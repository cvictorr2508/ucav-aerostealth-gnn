"""Configuration-disjoint train/validation/test splitting."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable

import numpy as np

DEFAULT_SEED = 42


@dataclass(frozen=True)
class SplitManifest:
    """Persistent description of one geometry-level dataset split."""

    seed: int
    train_ratio: float
    validation_ratio: float
    test_ratio: float
    train: tuple[str, ...]
    validation: tuple[str, ...]
    test: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "seed": self.seed,
            "ratios": {
                "train": self.train_ratio,
                "validation": self.validation_ratio,
                "test": self.test_ratio,
            },
            "configuration_ids": {
                "train": list(self.train),
                "validation": list(self.validation),
                "test": list(self.test),
            },
        }


def _validate_ratios(train: float, validation: float, test: float) -> None:
    ratios = np.asarray([train, validation, test], dtype=float)
    if np.any(ratios < 0.0):
        raise ValueError("Split ratios must be non-negative.")
    if not np.isclose(float(ratios.sum()), 1.0, atol=1e-12):
        raise ValueError("Train, validation, and test ratios must sum to 1.0.")


def split_configuration_ids(
    configuration_ids: Iterable[object],
    *,
    train: float = 0.70,
    validation: float = 0.15,
    test: float = 0.15,
    seed: int = DEFAULT_SEED,
) -> SplitManifest:
    """Split unique configuration IDs with a deterministic NumPy generator.

    Splitting is performed at configuration level so all nodes/conditions
    belonging to one geometry remain in exactly one subset.
    """

    _validate_ratios(train, validation, test)
    ids = sorted({str(value) for value in configuration_ids})
    if not ids:
        raise ValueError("At least one configuration_id is required.")

    rng = np.random.default_rng(seed)
    shuffled = np.asarray(ids, dtype=object)
    rng.shuffle(shuffled)

    n_total = len(shuffled)
    n_train = int(np.floor(train * n_total))
    n_validation = int(np.floor(validation * n_total))
    n_test = n_total - n_train - n_validation

    requested = [
        ("train", train, n_train),
        ("validation", validation, n_validation),
        ("test", test, n_test),
    ]
    for name, ratio, count in requested:
        if ratio > 0.0 and count == 0:
            raise ValueError(
                f"Split '{name}' received zero configurations; "
                "increase the dataset size or adjust the ratios."
            )

    train_ids = tuple(str(x) for x in shuffled[:n_train])
    val_start = n_train
    val_end = n_train + n_validation
    validation_ids = tuple(str(x) for x in shuffled[val_start:val_end])
    test_ids = tuple(str(x) for x in shuffled[val_end:])

    manifest = SplitManifest(
        seed=seed,
        train_ratio=float(train),
        validation_ratio=float(validation),
        test_ratio=float(test),
        train=train_ids,
        validation=validation_ids,
        test=test_ids,
    )

    all_ids = set(manifest.train) | set(manifest.validation) | set(manifest.test)
    if all_ids != set(ids):
        raise RuntimeError("Internal split error: configuration coverage changed.")
    if (
        set(manifest.train) & set(manifest.validation)
        or set(manifest.train) & set(manifest.test)
        or set(manifest.validation) & set(manifest.test)
    ):
        raise RuntimeError("Internal split error: configuration leakage detected.")

    return manifest


def write_split_manifest(manifest: SplitManifest, path: str | Path) -> Path:
    """Serialize the split manifest as stable, human-readable JSON."""

    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(manifest.to_dict(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return output

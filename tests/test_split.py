from ucav_aerostealth.data.split import split_configuration_ids


def test_reference_split_for_50_configurations_is_35_7_8():
    ids = [f"cfg-{i:02d}" for i in range(50)]
    split = split_configuration_ids(ids, seed=42)

    assert len(split.train) == 35
    assert len(split.validation) == 7
    assert len(split.test) == 8


def test_seed_42_is_deterministic_and_configuration_disjoint():
    ids = [f"cfg-{i:02d}" for i in range(20)]
    first = split_configuration_ids(ids, train=0.6, validation=0.2, test=0.2, seed=42)
    second = split_configuration_ids(ids, train=0.6, validation=0.2, test=0.2, seed=42)

    assert first == second
    assert not (set(first.train) & set(first.validation))
    assert not (set(first.train) & set(first.test))
    assert not (set(first.validation) & set(first.test))

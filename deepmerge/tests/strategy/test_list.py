import pytest
from deepmerge.strategy.list import ListStrategies
from deepmerge import Merger


@pytest.fixture
def custom_merger():
    return Merger(
        [
            (list, ListStrategies.strategy_append_unduplicated)
        ],
        [],
        [],
    )


def test_strategy_append_unduplicated(custom_merger):
    base = [1, 3, 2]
    nxt = [3, 5, 4, 1, 2]

    expected = [1, 3, 2, 5, 4]
    actual = custom_merger.merge(base, nxt)
    assert actual == expected

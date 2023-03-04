import pytest
from subsets import subsets

@pytest.mark.parametrize("input, expected", [([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
                                            ([0], [[],[0]])])
def testValidInput(input, expected):
    assert subsets(input).sort() == expected.sort()
import pytest
from subset_with_dups import subsetsWithDup

@pytest.mark.parametrize("input, expected", [([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
                                            ([0], [[],[0]])])
def testValidInput(input, expected):
    assert subsetsWithDup(input).sort() == expected.sort()
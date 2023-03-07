import pytest
from permute import permute

@pytest.mark.parametrize("input, expected", [([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
                                            ([0,1], [[0,1],[1,0]]),
                                            ([1],[[1]])])
def testValidInput(input, expected):
    assert permute(input).sort() == expected.sort()
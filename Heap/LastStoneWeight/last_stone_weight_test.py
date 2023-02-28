import pytest
from last_stone_weight import lastStoneWeight

@pytest.mark.parametrize("input, expected", [([2,7,4,1,8,1], 1), 
                                            ([1], 1)])
def testValidInput(input, expected):
    assert lastStoneWeight(input) == expected
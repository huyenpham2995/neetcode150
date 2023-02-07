import pytest
from two_sumII import two_sum

@pytest.mark.parametrize("input1, input2, expected", [([2,7,11,15], 9, [1,2]), 
                                            ([2,3,4], 6, [1,3]),
                                            ([-1,0], -1, [1,2]),
                                            ([], 10, [])])
def testValidInput(input1, input2, expected):
    assert two_sum(input1, input2) == expected
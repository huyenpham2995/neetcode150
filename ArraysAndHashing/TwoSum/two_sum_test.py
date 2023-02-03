import pytest
from two_sum import two_sum

@pytest.mark.parametrize("input1, input2, expected", [([2,7,11,15], 9, [0, 1]),
                                            ([3,2,4], 6, [1,2]),
                                            ([], 1, []),
                                            ([3, 3], 6, [0, 1])])
def testValidInput(input1, input2, expected):
    assert two_sum(input1, input2) == expected
import pytest
from k_closest import kClosest

@pytest.mark.parametrize("input1, input2, expected", [([[1,3],[-2,2]], 1, [[-2,2]]),
                                            ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]])])
def testValidInput(input1, input2, expected):
    assert kClosest(input1, input2) == expected
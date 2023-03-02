import pytest
from find_kth_largest import findKthLargest

@pytest.mark.parametrize("input1, input2, expected", [([3,2,1,5,6,4], 2, 5), 
                                            ([3,2,3,1,2,4,5,5,6], 4, 4),
                                            ([1], 5, 1)])
def testValidInput(input1, input2, expected):
    assert findKthLargest(input1, input2,) == expected
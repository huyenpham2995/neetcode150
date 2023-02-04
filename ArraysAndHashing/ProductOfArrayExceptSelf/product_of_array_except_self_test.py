import pytest
from product_of_array_except_self import product_except_self
                                            # this test case showed failure because they expected it to be the exact order, but we don't need to
@pytest.mark.parametrize("input, expected", [([1,2,3,4], [24,12,8,6]), 
                                            ([], []),
                                            ([-1,1,0,-3,3], [0,0,9,0,0])])
def testValidInput(input, expected):
    assert product_except_self(input) == expected
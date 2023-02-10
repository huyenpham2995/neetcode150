import pytest
from largest_rectangle import largest_rectangle

@pytest.mark.parametrize("input, expected", [([2,1,5,6,2,3], 10), 
                                            ([2,4], 4),
                                            ([], 0)])
def testValidInput(input, expected):
    assert largest_rectangle(input) == expected
import pytest
from max_area import max_area

@pytest.mark.parametrize("input, expected", [([1,8,6,2,5,4,8,3,7], 49), 
                                            ([1,1], 1),
                                            ([], 0)])
def testValidInput(input, expected):
    assert max_area(input) == expected
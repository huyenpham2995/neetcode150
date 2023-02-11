import pytest
from find_min import find_min

@pytest.mark.parametrize("input, expected", [([3,4,5,1,2], 1), 
                                            ([4,5,6,7,0,1,2], 0),
                                            ([11,13,15,17], 11),
                                            ([1], 1)])
def testValidInput(input, expected):
    assert find_min(input) == expected
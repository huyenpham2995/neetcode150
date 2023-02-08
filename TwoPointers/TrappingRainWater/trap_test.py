import pytest
from trap import trap

@pytest.mark.parametrize("input, expected", [([0,1,0,2,1,0,1,3,2,1,2,1], 6), 
                                            ([4,2,0,3,2,5], 9),
                                            ([], 0),
                                            ([1], 0)])
def testValidInput(input, expected):
    assert trap(input) == expected
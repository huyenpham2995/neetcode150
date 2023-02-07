import pytest
from three_sum import three_sum

@pytest.mark.parametrize("input, expected", [([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]), 
                                            ([0,1,1], []),
                                            ([], []),
                                            ([0,0,0], [[0,0,0]])])
def testValidInput(input, expected):
    assert three_sum(input) == expected
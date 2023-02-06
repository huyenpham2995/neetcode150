import pytest
from longest_consecutive_sequence import longest_consecutive

@pytest.mark.parametrize("input, expected", [([100,4,200,1,3,2], 4), 
                                            ([0,3,7,2,5,8,4,6,0,1], 9),
                                            ([], 0),
                                            ([1], 1)])
def testValidInput(input, expected):
    assert longest_consecutive(input) == expected
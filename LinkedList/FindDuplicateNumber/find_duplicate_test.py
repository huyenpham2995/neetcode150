import pytest
from find_duplicate import find_duplicate

@pytest.mark.parametrize("input, expected", [([1,3,4,2,2], 2),
                                            ([3,1,3,4,2], 3),
                                            ([1,1], 1)])
def testValidInput(input, expected):
    assert find_duplicate(input) == expected
import pytest
from find_median import find_median

@pytest.mark.parametrize("input1, input2, expected", [([1,3], [2], 2.0),
                                            ([1,2], [3,4], 2.5)])
def testValidInput(input1, input2, expected):
    assert find_median(input1, input2) == expected
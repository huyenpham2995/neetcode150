import pytest
from min_eating_speed import min_eating_speed

@pytest.mark.parametrize("input1, input2, expected", [([3,6,7,11],8, 4),
                                            ([30,11,23,4,20], 5, 30),
                                            ([30,11,23,4,20], 6, 23)])
def testValidInput(input1, input2, expected):
    assert min_eating_speed(input1, input2) == expected
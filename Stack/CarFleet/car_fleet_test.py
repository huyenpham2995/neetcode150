import pytest
from car_fleet import car_fleet

@pytest.mark.parametrize("input1, input2, input3, expected", [(12, [10,8,0,5,3], [2,4,1,1,3], 3), 
                                            (10, [3], [3], 1),
                                            (100, [0,2,4], [4,2,1],1)])
def testValidInput(input1, input2, input3, expected):
    assert car_fleet(input1, input2, input3) == expected
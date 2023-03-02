import pytest
from least_interval import leastInterval

@pytest.mark.parametrize("input1, input2, expected", [(["A","A","A","B","B","B"], 2, 8), 
                                            (["A","A","A","B","B","B"], 0, 6),
                                            (["A","A","A","A","A","A","B","C","D","E","F","G"], 2, 16)])
def testValidInput(input1, input2, expected):
    assert leastInterval(input1, input2,) == expected
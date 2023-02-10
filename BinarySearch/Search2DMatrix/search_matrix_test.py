import pytest
from search_matrix import search_matrix

@pytest.mark.parametrize("input1, input2, expected", [([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True), 
                                            ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 12, False),
                                            ([], 0, False)])
def testValidInput(input1, input2, expected):
    assert search_matrix(input1, input2) == expected
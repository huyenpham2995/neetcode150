import pytest
from search import search

@pytest.mark.parametrize("input1, input2, expected", [([4,5,6,7,0,1,2], 0, 4),
                                            ([4,5,6,7,0,1,2], 3, -1),
                                            ([], 1, -1),
                                            ([1], 0, -1)])
def testValidInput(input1, input2, expected):
    assert search(input1, input2) == expected
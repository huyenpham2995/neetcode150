import pytest
from word_search import exist

@pytest.mark.parametrize("input1, input2, expected", [([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
                                            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
                                            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False)])
def testValidInput(input1, input2, expected):
    assert exist(input1, input2) == expected
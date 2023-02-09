import pytest
from eval_rpn import eval_RPN

@pytest.mark.parametrize("input, expected", [(["2","1","+","3","*"], 9), 
                                            (["4","13","5","/","+"], 6),
                                            ([], 0),
                                            (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)])
def testValidInput(input, expected):
    assert eval_RPN(input) == expected
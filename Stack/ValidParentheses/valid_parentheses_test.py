import pytest
from valid_parentheses import is_valid

@pytest.mark.parametrize("input, expected", [("()", True), 
                                            ("()[]{}", True),
                                            ("(]", False)])
def testValidInput(input, expected):
    assert is_valid(input) == expected
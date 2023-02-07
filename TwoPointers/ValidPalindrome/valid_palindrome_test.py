import pytest
from valid_palindrome import is_palindrome

@pytest.mark.parametrize("input, expected", [("A man, a plan, a canal: Panama", True), 
                                            ("race a car", False),
                                            (" ", True)])
def testValidInput(input, expected):
    assert is_palindrome(input) == expected
import pytest
from longest_non_repeating_substring import longest_non_repeating_substring

@pytest.mark.parametrize("input, expected", [("abcabcbb", 3), 
                                            ("bbbbb", 1),
                                            ("", 0),
                                            ("a", 1),
                                            ("pwwkew", 3)])
def testValidInput(input, expected):
    assert longest_non_repeating_substring(input) == expected
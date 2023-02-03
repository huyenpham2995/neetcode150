import pytest
from valid_anagram import valid_anagram

@pytest.mark.parametrize("input1, input2, expected", [("anagram", "nagaram", True),
                                                      ("rat", "car", False),
                                                      ("", "", True),
                                                      ("", "abc", False)
                                                     ])
def testValidInput(input1, input2, expected):
    assert valid_anagram(input1, input2) == expected

import pytest
from character_replacement import character_replacement

@pytest.mark.parametrize("input1, input2, expected", [("ABAB", 2, 4),
                                            ("AABABBA", 1, 4),
                                            ("", 1, 0),
                                            ("A", 5, 1)])
def testValidInput(input1, input2, expected):
    assert character_replacement(input1, input2) == expected
import pytest
from partition import partition

@pytest.mark.parametrize("input, expected", [("aab", [["a","a","b"],["aa","b"]]),
                                            ("a", [["a"]])])
def testValidInput(input, expected):
    assert partition(input).sort() == expected.sort()
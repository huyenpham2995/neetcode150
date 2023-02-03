import pytest
from group_anagrams import group_anagrams
                                            # this test case showed failure because they expected it to be the exact order, but we don't need to
@pytest.mark.parametrize("input, expected", [(["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]), 
                                            ([""], [[""]]),
                                            (["a"], [["a"]])])
def testValidInput(input, expected):
    assert group_anagrams(input) == expected
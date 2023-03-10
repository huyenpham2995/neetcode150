import pytest
from letter_combination import letterCombinations

@pytest.mark.parametrize("input, expected", [("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
                                            ("", []),
                                            ("2",["a","b","c"])])
def testValidInput(input, expected):
    assert letterCombinations(input) == expected
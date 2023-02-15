import pytest
from check_inclustion import check_inclusion1, check_inclusion2, check_inclusion3

@pytest.mark.parametrize("input1, inoput2, expected", [("ab", "eidbaooo", True), 
                                            ("ab", "eidboaoo", False),
                                            ("dcda", "adc", True)])
def testValidInput(input1, input2, expected):
    assert check_inclusion1(input1, input2) == expected
    assert check_inclusion2(input1, input2) == expected
    assert check_inclusion3(input1, input2) == expected
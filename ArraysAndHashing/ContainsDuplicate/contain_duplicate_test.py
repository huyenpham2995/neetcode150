import pytest
from contain_duplicate import containsDuplicate1, containsDuplicate2

@pytest.mark.parametrize("input,expected", [([1,2,3,1], True),
                                            ([1,2,3,4], False),
                                            ([], False),
                                            ([0], False),
                                            ([1,1,1,3,3,4,3,2,4,2], True)])
def testValidInput(input, expected):
    assert containsDuplicate1(input) == expected
    assert containsDuplicate2(input) == expected
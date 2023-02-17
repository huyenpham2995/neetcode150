import pytest
from reorder_list import reorder_list1, reorder_list2

@pytest.mark.parametrize("input, expected", [([1,2,3,4], [1,4,2,3]),
                                            ([1,2,3,4,5], [1,5,2,4,3]),
                                            ([], [])])
def testValidInput(input, expected):
    assert reorder_list1(input) == expected
    assert reorder_list2(input) == expected

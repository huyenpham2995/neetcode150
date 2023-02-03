import pytest
from top_k_frequent_elements import top_k_frequent_with_sort, top_k_frequent_with_bucket_list

@pytest.mark.parametrize("input1, input2, expected", [([1,1,1,2,2,3], 2, [1,2]),
                                            ([], 2, []),
                                            ([1], 1, [1])])
def testValidInput(input1, input2, expected):
    assert top_k_frequent_with_sort(input1, input2) == expected
    assert top_k_frequent_with_bucket_list(input1, input2) == expected
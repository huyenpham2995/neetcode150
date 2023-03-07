import pytest
from combination_sum import combinationSum

@pytest.mark.parametrize("input1, input2, expected", [([2,3,6,7], 7, [[2,2,3],[7]]),
                                            ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
                                            ([2], 1, [])])
def testValidInput(input1, input2, expected):
    assert combinationSum(input1, input2).sort() == expected.sort()
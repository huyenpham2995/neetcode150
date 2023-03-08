import pytest
from combination_sumII import combinationSum2

@pytest.mark.parametrize("input1, input2, expected", [([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
                                            ([2,5,2,1,2], 5, [[1,2,2],[5]]),
                                            ([2], 1, [])])
def testValidInput(input1, input2, expected):
    assert combinationSum2(input1, input2).sort() == expected.sort()
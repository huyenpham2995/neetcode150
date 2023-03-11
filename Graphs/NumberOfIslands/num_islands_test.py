import pytest
from num_islands import numIslands

@pytest.mark.parametrize("input, expected", [([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], 1),
([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
], 3),
([["0","1","0"],["1","0","1"],["0","1","0"]],4),
([],0)])

def testValidInput(input, expected):
    assert numIslands(input) == expected
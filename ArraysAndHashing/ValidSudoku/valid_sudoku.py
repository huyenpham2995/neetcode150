from typing import List
from collections import defaultdict

def is_valid_sudoku(board: List[List[str]]) -> bool:
    #key is the row, value is the list of numbers in that row
    row_dict = defaultdict(list)
    #key is the column, value is the list of numbers in that column
    col_dict = defaultdict(list)
    # key is [row/3,col/3] of the small 3x3 board, value is the list of numbers in that small board
    small_board_dict = defaultdict(list)

    for row in range(9):
        for col in range(9):
            cur_val = board[row][col]
            if cur_val != ".":
                if (cur_val in row_dict[row]
                    or cur_val in col_dict[col]
                    or cur_val in small_board_dict[(row//3, col//3)]):
                    return False
                row_dict[row].append(cur_val)
                col_dict[col].append(cur_val)
                small_board_dict[(row//3, col//3)].append(cur_val)
    
    return True
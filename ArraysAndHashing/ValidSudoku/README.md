### Question
- Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
- Note:
    - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned rules.
- [Link to question.](https://leetcode.com/problems/valid-sudoku/description/)

### Thoughts
- Input and output:
    - Input: a 9x9 array represents a sudoku board.
    - Output: boolean, if the board is valid or not.
- Keep track of the numbers appear on each row. If the number already appears in a row, thats a duplicate -> false.
- Same thing with each column.
- A bit of a tricky case is the smaller 3x3 board.
    - The big board is divided into 9 smaller 3x3 board. 
    - To see the number belongs to which smaller box, we need to take its "cordinate" and divide by 3, take the division.
    - Example: 
        - row 3 column 3 (with index 0, it's row 2 column 2), belong to 2//3 = 0, 2//3 = 0 => small board (0,0)
        - row 4 column 3 (with index 0, it's row 3 column 2), belong to 4//3 = 1, 2//3 = 0 => small board (1,0)
    - Keep the list of all numbers in the smaller board, if there's duplicate => invalid.
- Ignore "."

### Pseudocode
- Initialize variables:
    - A dictionary for row values, with key = row number, value = list of all numbers in that row.
    - A dictionary for column values, with key = col number, value = list of all numbers in that column.
    - A dictionary for the 3x3 smaller board, with key = (row//3, col//3),  value = list of all numbers in that smaller board.
- Loop through the row
    - Loop through the column
        - If the value in the grid is not "."
            - Check to see if it's in the row_dict, col_dict, smaller_board_dict:
                - If yes, return False
            - If it's not in those 3, add the value to those dict
- At the end, if nothing is duplicated, return True.

### BigO
Time complexity O(N^2)


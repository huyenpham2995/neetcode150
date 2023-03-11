from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    path = set()

    def backtrack(row,col,word):
        if word == "":
            return True
        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or (row,col) in path or board[row][col] != word[0]:
            return False
        
        path.add((row,col))
        res = (backtrack(row-1,col,word[1:]) or backtrack(row+1,col,word[1:]) or backtrack(row,col-1,word[1:]) or backtrack(row,col+1,word[1:]))
        path.remove((row,col))

        return res
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i,j,word):
                return True
    return False

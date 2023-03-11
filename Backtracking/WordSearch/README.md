### Question
- [Link to question.](https://leetcode.com/problems/word-search/description/)

### Thoughts
- Input and output:
    - Input: 
        - the word "board"(2D array)
        - the word we want to search for (string)
    - Output: boolean, if the word exists in the board.
- If the word is empty, then it exists in the board.
- At 1 position, there are at most 4 ways to go: up, down, left, right.
- We can go through the board one by one to find a box that matches the first letter of the word. Once we find it, we have 4 options as mentioned above to determine the next move. Recursively doing that until we reaches the end of the word if it exists, or just exhaust all searches and conclude that the word is not in the board.
- As we go along, we need to mark the path we have checked to make sure we don't go into a loop of search.
- Example: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    - row=0   
        - col=0: A != S, pass
        - col=1: B != S, pass
        - col=2: C != S, pass
        - col=3: E != S, pass
    - row=1:
        - col=0: S==S
            - add (1,0) to mark the path
            - Go up to (0,0): A != E, return False
            - Go down to (2,0): A != E, return False
            - Go left, no way left since col=-1 go out of range, return False
            - Go right, F != E, return False
            - remoe (1,0) out of the path
        - col=1: F!=S, pass
        - col=2: C!=S, pass
        - col=3: S==S
            - add (1,3) to mark the path
            - Go up to (0,3): E == E
                - Go up from (0,3), row=-1 out of range, return False
                - Go right from (0,3), col=4 go out of range, return False
                - Go down from (0,3), (1,3) is in the path, return False
                - Go left from (0,3), C !=E, return False
            - Go down to (2,3): E == E
                - Go up from (2,3), (1,3) is in the path, return False
                - Go right, out of range
                - Go left to (2,2), E==E
                    - Found all letters of the searching word, return True!
    - Return True

### Pseudocode
- Initialize: path = set()
- Create a recursion backtrack function, taking in row, col and the word we want to search
    - if the word is "", return True
    - if row or col < 0  or row >= # of row (len(board)) or col >= # of columns (len(board[0])) or board[row][col] is not word[0]: return False
    - If none of those were violated, we know we found a potential path
        - Add the (row, col) to the path
        - Recursively call backtrack with 4 options, and with the word excluding the first character (the current position already matches the first character):
            - row-1, col, word[1:]
            - row +1, col, word[1:]
            - row, col-1, word[1:]
            - row, col+1, word[1:]
        - After exhausting all 4 directions, remove this position out of the path to search for another path (assuming it did not match the word).
        - return the result
- Go through each character of each row
    - Go through each character of each col
        - call backtrack with row, col and word, if it's true then return true
- Return False.

### BigO
- Go through the whole board takes MxN time (M = # of rows, N = # of columns).
- At each spot, there are 4 ways to go => 4^N at each spot (assuming N>M)
=> O(M*N*4^N)

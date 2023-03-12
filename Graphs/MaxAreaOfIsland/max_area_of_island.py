from typing import List
from collections import deque

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    visited = set()
    max_area = 0 

    def bfs(row,col):
        q = deque()
        q.append((row,col))
        area = 0
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            r,c = q.popleft()
            area += 1

            for x,y in direction:
                if r+x in range(len(grid)) and c+y in range(len(grid[0])) and grid[r+x][c+y] == 1 and (r+x,c+y) not in visited:
                    q.append((r+x,c+y))
                    visited.add((r+x,c+y))

        return area

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row,col) not in visited:
                visited.add((row,col))
                area = bfs(row,col)
                if area > max_area:
                    max_area = area
    
    return max_area
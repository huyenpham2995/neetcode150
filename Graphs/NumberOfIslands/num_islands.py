from typing import List

def numIslands(grid: List[List[str]]) -> int:
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r,c) not in visited:
                visited.add((r,c))
                island = [(r,c)]
                direction = [[-1,0], [1,0], [0,-1], [0,1]]
                while island:
                    row,col = island.pop(0)
                    for x,y in direction:
                        if row + x in range(len(grid)) and col + y in range(len(grid[0])) and (row+x,col+y) not in visited and grid[row+x][col+y] == "1":
                            island.append((row+x,col+y))
                            visited.add((row+x,col+y))
                count += 1

    return count
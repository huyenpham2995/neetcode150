### Question
- [Link to question.](https://leetcode.com/problems/number-of-islands/description/)

### Thoughts
- Input and output:
    - Input: a grid showing the area, with 1 as land and 0 as water
    - Output: the number of islands.
- What if the grid is empty? There's 0 island.
- Island is formed by connecting the "1"s from vertical and horizontal "lands". What we can do is to find a "land", then from there doing a BFS to find all other lands connecting to it. Once we exhausted all the lands and encounter new land, that's the beginning of a 2nd island and so on.
- There are 4 ways we can go once we find a land: up, down, left, right.
    - We only want to visit the node with valid coordination. That's it, the index of row and column is larger than 0, row < num of rows and col < num of columns.
    - We only want to visit another land, which mean the node value is 1.
- When we visit a node, we mark it as visited so we don't investigate it next time we encounter it.
- Example: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    - At (0,0), we find a land. From there, do a BFS search to find all the connecting land. Add (0,0) to visited list. Increase the count of land to 1
        - We cannot go up or left. 
        - We go right (0,1), it's a land so add it to the visited list and to the queue.
        - We go down (1,0), it's also a land so add it to the visited list and to the queue
        - Pop (0,1) out of list, investigate its neighbor (0,2) and (1,1). They are both lands, so add that to the visited list and to the queue.
        - Pop (1,0) out of list, investigate its neighbor (1,1) and (2,1). Since (1,1) is already visited, we don't do anything to it. add (2,1) to the list.
    ... Continue like that until we investigate all the nodes in the grid.

### Pseudocode
- Initialize:
    - visited = empty set, to keep track of all node that has been visited
    - count = 0: count of islands
- Loop through each row
    - Loop through each column
        - if the current node has not been visited and it is a land
            - add it to the visited set
            - add it to the queue
            - When the queue is not empty (bfs):
                - Pop the first node out of the queue
                - Investigate its 4 neighbors: if the indexes are valid, the node is a land and it has not been visited
                    - add it to the queue
                    - add it to the visited set
        - Once we reach here, we have exhausted all connected lands. update count += 1 as this is an island.
- return count.

### BigO
- Go through all nodes in the grid: MxN time (M=# of rows, N=num of columns).
- At each node we have 4 options to go.

### Question
- [Link to question.](https://leetcode.com/problems/max-area-of-island/description/)

### Thoughts
- Input and output:
    - Input: a grid showing the area, with 1 as land and 0 as water
    - Output: the max area of the island.
- This is very similar to number of island question, but instead of counting the island, we keep track of the biggest area of the island.
- Similar process: once we find a "land", using bfs to travel to the connected land. Each time we find a connected land, we add 1 to the area of that land. Once we have travelled through the entire island, compare the are of that area to the current max island and update if needed.

### Pseudocode
- If gird is empty, return 0 (no island).
- Initialize:
    - max_area = 0
    - visited = empty set: keep track of all visited nodes.
- Create a bfs function to find the connecting lands, which takes in the cordinations (row and column index)
    - Create a queue to keep track of all neighbors of the current node.
    - Set area of this island = 0
    - 4 directions to go: up, down, left, right, i.e [[-1,0],[1,0],[0,-1],[0,1]]
    - While the queue is not empty (i.e: there are still neigbors to visit)
        - pop the first element out of the queue
        - area += 1
        - exploring all 4 neighbors: if the cordinates are in bound, the node has not been visited and the grid at that cordinate is a land:
            - Add the cordinate to the queue
            - Add the node at that cordinate to visited set.
    - Once the queue is empty, that means we have visted the entire island, return its area.
- Go through all the row of the grid
    - Go through all the columns of the grid
        - If the current node has not been visited and it's a land, we know that we are exploring a new island
            - Add this current node cordination to the visited set
            - call bfs on this node to get the area of this island.
            - Compare the area of this island with the max_area and update as needed.
- return max_area

### BigO
- Go through all nodes in the grid: MxN time (M=# of rows, N=num of columns).
- At each node we have 4 options to go, but we only go to the direction of the unvisited node.

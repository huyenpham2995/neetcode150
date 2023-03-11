### Question
- [Link to question.](https://leetcode.com/problems/clone-graph/description/)

### Thoughts
- Input and output:
    - Input: a starting node of the original graph.
    - Output: the starting node of the deep copy graph of the original graph.
- If the node is empty, meaning graph is empty, just return None.
- This is pretty similar to copying linked list.
- We need a dictionary to keep track of the copies that have been created for the nodes. Key: original node, value: deep copy of that node.
- Will use BFS.

### Pseudocode
- if node is None, return None
- Initialize:
    - dictionary with key as original node, value as the copy
    - A queue to keep track of all visited node.
    - Add node to the queue
- While queue is not empty:
    - pop the first node out of queue
    - if node has not had a copy, create a copy with its value
    - go through all the neighbors of the node
        - if neigbor does not have a copy
            - create its copy
            - add node-copy to the dictionary
            - append the original node to the queue
        - append the copy of the neighbor to the neighbors list of the copied node.

### BigO
- Visit all nodes once => O(N).
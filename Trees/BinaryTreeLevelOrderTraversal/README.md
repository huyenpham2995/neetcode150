### Question
- [Link to question.](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: a list of the nodes value, group by the the level traversal of the tree.
- This is basically BFS but we need to keep track the nodes at each level.
- If the tree is empty then just return an empty list.
- We start from the root. Append the value of root to the result. Then check to see if root has a left child or a right child. If it does, add the left child to the queue first, then right child.
- The next round consists of 2 nodes to process (left and right). Go through the list of the nodes to process, add their value to a list, then if they have a left and/or right child, add them to the queue to process at the next round. append the value list to the result list.
- Basically at each round, all the node at a current level will be processed. Their children will be processed on the next round and so on.

### Pseudocode
- Check to see if root is None, if it is return [].
- Create a queue for processing and a res list.
- When the queue is not empty:
    - Create a local list l to hold the value of all the nodes that are processed in this round.
    - Create a local list of next_q to hold the list of nodes to be processed on next round.
    - Go through the list of nodes that we need to process in this round:
        - Append the value of the node to l.
        - If it has a left child append it to next_q.
        - If it has a right child append it to next_q.
    - Set q = next_q
    - Append the list of values that were processed at this round to res.
    
### BigO
- O(N).


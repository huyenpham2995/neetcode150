### Question
- [Link to question.](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

### Thoughts
- Input and output: 
    - Input: 
        - Root of a binary tree.
        - Node p of the tree.
        - Node q of the tree.
    - Output: the lowest common ancestor (the lowest node that has both p and q as descendants).
- If the tree is empty then return None.
- My thoughts: when we travel across the tree to reach the 2 nodes, that path will cross at some point, and that point is the ancestor of both node. The "highest ancestor" by default is the root (both nodes for sure will be the descendants of the root).
- What we can do is having 2 pointers, 1 travel to find p, 1 to find q. On the way to the 2 nodes, whenever p and q meet each other, we note that met node and continue, until either pointer reaches its destination. The most recent met point will be the lowest ancestor of both nodes.

### Pseudocode
- If the root is None, return True.
- Initialize variables:
    - met = p1 = q1 = root.
- Go through the root while p1 and q1 have not met p and q:
    - Travel p1 towards p (base on p1 and p value, decide to move left or right).
    - Travel q1 towards q (base on q1 and q value, decide to move left or right).
    - Check to see if p1 == q1, if they are update met.
 - Return met.

### BigO
O(N) (at most going through the whole tree once).
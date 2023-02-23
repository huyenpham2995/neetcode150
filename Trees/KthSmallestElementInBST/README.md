### Question
- [Link to question.](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

### Thoughts
- Input and output: 
    - Input: 
        - root of a binary tree.
        - interger k, represent the kth smallest (1-indexed).
    - Output: count of the good nodes in the tree (there's no node from the path from root to this node that is > than this node).
- Basically this is an Inorder traversal: left-root-rihght.
- Go all the way to the left of the tree, take the left node first, then root, then right, before moving up, until we reach k nodes in the list.
    - Why? the left side of the tree  contains the smallest element in the BST. We know that all nodes from the left subtree will be smaller than the root, so we have to explore the left first before going right.
    - I was stuck at using DFS and recursion, but there's a way for DFS and stack that is way easier to understand.
- Go all the way to the left of the tree. Each time we move, we put the node inside the stack. So when we reached the "last" left node, that one is on top of the stack.
- Pop it out of the stack. decrement k (we have found the 1st smallest element.)
- Then add the move the pointer to that the right side of that node, before moving "up" (the 2nd left node).
- Keep doing that until k=0, return the current node value.

### Pseudocode
- Initialize variables:
    - Stack = []
    - cur = root
- while stack is not empty or cur is not null (just one of the two, because they will be during execution)
    - Travel all the way to the left (cur.left not None):
        - Add node to stack
        - cur = cur.left
    - (Get here when cur is None): pop top out of stack
    - Decrement k
    - check if k==0, if it is return node.val
    - if it's not, cur = cur.right (move right)

### BigO
- O(N)


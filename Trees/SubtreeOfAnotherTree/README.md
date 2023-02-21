### Question
- [Link to question.](https://leetcode.com/problems/balanced-binary-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of 2 binary trees.
    - Output: boolean, if one tree is the subtree of the other.
- If the subtree is None, then return True since an empty tree is the subtree of every tree.
- If the main tree is empty and the subtree is not, then return False.
- At each node, check to see if the current subtree which have the current node as root has the same structure as the subtree. We do this by calling [isSameTree](https://github.com/huyenpham2995/neetcode150/tree/main/Trees/SameTree) on the current node and subRoot. If it is, return True, if it's not, check to see whether the subtree on the left or on the right contains the subtree.

### Pseudocode
- If root is None and subRoot is not, return False.
- Call isSameTree on root and subRoot, if it's true, return True.
- If not, recursively call isSubtree on the left and right node. If either of them are true, then return True, else False.

### BigO
- O(MxN), with M being the number of nodes of the subtree, and N is the number of node of the main tree. At each node, we are checking to see if the subtree with that node being root being the same as the subtree. So at most we are going through M node at each nth node.
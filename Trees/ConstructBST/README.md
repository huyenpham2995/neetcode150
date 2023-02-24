### Question
- [Link to question.](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

### Thoughts
- Input and output: 
    - Input: 
        - An array represent inorder traversal of a binary tree.
        - An array represent preorder traversal of a binary tree.
    - Output: the tree (root node)
- Pre-order: root-left-right. In-order:left-root-right.
- If either or both of those array is empty, then return None.
- From preorder, we know the first element of the array is the root of the tree. Don't have information about the rest tho.
- That's when we need the in-order tree.
- Example: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    - The root is 3, since that's the first element in preorder. We don't know about the left and right child just based on the preorder array.
        - Then we look at the inorder array. The left subtree is on the left of 3 ([9]) and has 1 element, the right subtree is on the right of 3 ([15,20,7]), which has 3 elements. 
        - Create a tree node for 3, and then recursively construct the left and right subtree. To do this, we need to construct the preorder list and the inorder list for the left and right subtree.
            - We know 3 is at index 1 in the inorder array. That means, the left subtree nodes are at inorder[0:root_index], the right subtree nodes are at inorder[root_index+1:].
            - We also know there  is 1 node on the left subtree, so they are in preorder[0:root_index+1] (since list slicing is exclusive at the last element). The rest excluding the root belongs to the right subtree, so preorder[root_index+1:].
        - Go on like that until the end of preorder list.

### Pseudocode
- If either list is empty, return None
- Create the tree node for root: root = TreeNode(preorder[0]) (since the first node is always the root in preorder list).
- Find the index of this root node in the inorder list.
- Recrusively construct the left and right tree:
    - root.left = calling the function with preorder[:index+1], inorder[0:index]
    - root.right = calling the function with preorder[index+1:], inorder[index+1:]
    
### BigO
- O(N)


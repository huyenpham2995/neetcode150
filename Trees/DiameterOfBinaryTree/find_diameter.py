from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def diameterOfBinaryTree1(root: Optional[TreeNode]) -> int:
    diameter = maxDepth(root.left) + maxDepth(root.right)
    return max(diameterOfBinaryTree1(root.left), diameterOfBinaryTree1(root.right), diameter)

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None: return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def diameterOfBinaryTree2(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(root: Optional[TreeNode]):
        nonlocal res
        if root is None: return 0

        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left+right)

        return 1 + max(left,right)    
    dfs(root)
    return res

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth1(root: Optional[TreeNode]) -> int:
    if root == None: return 0

    return 1 + max(max_depth1(root.left), max_depth1(root.right))

# TODO: iterative method using stack
def max_depth2(root: Optional[TreeNode]) -> int:
    pass
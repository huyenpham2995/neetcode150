from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isValidBST(root: Optional[TreeNode]) -> bool:

    def checkBST(root: Optional[TreeNode], left: int, right: int):
        if root is None: return True

        if not (left<root.val<right):
            return False

        return checkBST(root.left, left, root.val) and checkBST(root.right, root.val,right)
        
    return checkBST(root, float("-inf"), float("inf"))
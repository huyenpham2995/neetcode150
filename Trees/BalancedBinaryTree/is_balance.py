from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def isBalanced(root: Optional[TreeNode]) -> bool:
    if root is None: return True
    diff = 0

    def get_height(root: Optional[TreeNode]):
        nonlocal diff
        if root is None: return 0

        left = get_height(root.left)
        right = get_height(root.right)
        diff = max(diff, abs(left-right))
        return 1 + max(right,left)

    get_height(root)
    if diff > 1:
        return False
    return True
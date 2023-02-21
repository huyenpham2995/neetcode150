from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root is None and subRoot: return False

    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is None: return True
            else: return False
        else:
            if q is None: return False

        if p.val != q.val: return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
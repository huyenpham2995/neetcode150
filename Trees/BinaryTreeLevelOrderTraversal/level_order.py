from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None: return []

    q = [root]
    res = []

    while q:
        l = []
        next_q = []
        for node in q:
            l.append(node.val)
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
        q = next_q
        res.append(l)
    
    return res
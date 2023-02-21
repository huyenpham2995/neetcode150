from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if root is None: return []

    res = []
    q = [root]

    while q:
        res.append(q[0].val)
        next_q = []

        for node in q:
            if node.right:
                next_q.append(node.right)
            if node.left:
                next_q.append(node.left)
            q = next_q
    
    return res
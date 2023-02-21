# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None: return None

    p1 = q1  = met = root

    while p1.val != p.val and q1.val != q.val:
        if p.val < p1.val:
            p1 = p1.left
        else:
            p1 = p1.right

        if q.val < q1.val:
            q1 = q1.left
        else:
            q1 = q1.right
        
        if p1 == q1:
            met = p1
    
    return met
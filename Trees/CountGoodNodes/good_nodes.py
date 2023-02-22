# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes1(root: TreeNode) -> int:
    if root is None: return 0
    q = [(root, root.val)]
    count = 0

    while q:
        node, max_val = q.pop(0)
        if node.val >= max_val:
            count += 1
        if node.left:
            q.append((node.left, node.left.val if node.left.val > max_val else max_val))
        if node.right:
            q.append((node.right, node.right.val if node.right.val > max_val else max_val))
    
    return count

def goodNodes2(root: TreeNode) -> int:
    def dfs(root, max_val):
        if root is None: return 0
        res = 1 if root.val >= max_val else 0
        max_val = root.val if root.val > max_val else max_val

        res += dfs(root.left, max_val)
        res += dfs(root.right, max_val)

        return res
    
    return dfs(root,root.val)
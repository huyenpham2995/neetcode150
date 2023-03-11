from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node: return None

    nodes_dict = {}
    q = deque()
    q.append(node)

    while q:
        n = q.popleft()

        if not nodes_dict.get(n):
            nodes_dict[n] = Node(n.val)
        for neighbor in n.neighbors:
            if not nodes_dict.get(neighbor):
                q.append(neighbor)
                neighbor_copy = Node(neighbor.val)
                nodes_dict[neighbor] = neighbor_copy
            nodes_dict[n].neighbors.append(nodes_dict[neighbor])

    return nodes_dict[node]
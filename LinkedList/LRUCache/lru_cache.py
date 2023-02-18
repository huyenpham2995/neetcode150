# doubly linked list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.pre, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.LRU_dict = {}

        # insert on the left of dummy_right node
        # remove from the right of dummy_left node
        self.left_dummy, self.right_dummy = Node(0,0), Node(0,0)
        self.left_dummy.next, self.right_dummy.pre = self.right_dummy, self.left_dummy

    def insert(self, node: Node):
        self.right_dummy.pre.next = node
        node.pre = self.right_dummy.pre
        self.right_dummy.pre = node
        node.next = self.right_dummy
    
    def remove(self, node: Node):
        node.next.pre = node.pre
        node.pre.next = node.next     

    def get(self, key: int) -> int:
        if self.LRU_dict.get(key) == None:
            return -1
        else:
            self.remove(self.LRU_dict[key])
            self.insert(self.LRU_dict[key])
            return self.LRU_dict[key].val
        
    def put(self, key: int, value: int) -> None:
        if self.LRU_dict.get(key) == None:
            self.LRU_dict[key] = Node(key,value)
            self.insert(self.LRU_dict[key])
        else:
            self.remove(self.LRU_dict[key])
            self.LRU_dict[key] = Node(key,value)
            self.insert(self.LRU_dict[key])
        
        if len(self.LRU_dict) > self.limit:
            node = self.left_dummy.next
            self.remove(node)
            del self.LRU_dict[node.key]
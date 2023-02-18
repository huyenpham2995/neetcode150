from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head: return False

    slow, fast = head, head.next

    while fast and fast.next:
        if slow == fast:
            return True 

        slow = slow.next
        fast = fast.next.next
    
    return False
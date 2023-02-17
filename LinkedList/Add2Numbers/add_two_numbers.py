from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    p1, p2 = l1, l2
    carry = 0

    while p1 and p2:
        total = p1.val + p2.val + carry
        cur.next = ListNode(total % 10)

        carry = 1 if total > 9 else 0
        cur = cur.next
        p1 = p1.next
        p2 = p2.next

    while p1:
        total = p1.val + carry
        cur.next = ListNode(total % 10)
        carry = 1 if total > 9 else 0
        cur = cur.next
        p1 = p1.next
    
    while p2:
        total = p2.val + carry
        cur.next = ListNode(total % 10)
        carry = 1 if total > 9 else 0
        cur = cur.next
        p2 = p2.next
    
    if carry: 
        cur.next = ListNode(1)
    
    return dummy.next
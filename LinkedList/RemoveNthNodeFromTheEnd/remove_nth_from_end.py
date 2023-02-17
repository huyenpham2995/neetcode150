from typing import List, Optional

def remove_nth_from_end(head: Optional[List], n: int) -> Optional[List]:
    dummy = ListNode(0, head)
    right = head

    for _ in range(n):
        right = right.next
    
    pre = dummy
    left = head

    while right:
        pre = left
        left = left.next
        right = right.next
    
    pre.next = pre.next.next
    
    return dummy.next

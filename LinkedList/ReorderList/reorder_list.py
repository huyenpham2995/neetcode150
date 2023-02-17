from typing import List, Optional

def reorder_list1(head: Optional[List]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    nodes = []
    count = 0

    cur = head
    while cur:
        nodes.append(cur)
        cur=cur.next
        count += 1

    half = count//2

    cur = head
    for i in range(half):
        node = nodes.pop()
        nxt = cur.next
        cur.next = node
        node.next = nxt
        cur = nxt

    cur.next = None

def reorder_list2(head: Optional[List]) -> None:
    slow = fast = head

    # find the middle of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the 2nd half
    cur = slow.next
    slow.next = pre = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    cur1 = head
    cur2 = pre

    # connect the 1st half and the 2nd half
    while cur1 and cur2:
        nxt1 = cur1.next
        nxt2 = cur2.next
        cur1.next = cur2
        cur2.next = nxt1
        cur1 = nxt1
        cur2 = nxt2
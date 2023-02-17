### Question
[Link to question.](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

### Thoughts
- Input and output:
    - Input: 
        - a linked list.
        - number N, indicate the Nth position from the end to remove.
    - Output: the head of the linked list after nth node from the end is removed.
- I reallyyyyyyyyyy overcomplicated it: find the mid node, then calculate position from the mid node lalalala.
- Realistically, just need 2 pointer. 
    - First round move the right pointer to the nth position of the linked list (from the beginning).
    - Let the left pointer starts at head. While the right iis still able to move (not the end of linked list yet), move both right and left pointer 1 spot ahead.
    - When right pointer reached the end, left pointer will be at the Nth node from the end.
    - Special case: when the node we want to remove is at the beginning of the linked list. We will need to update the head before delete the head.
        - This depends on if there's any element after head. If there is, move head to the 2nd one in the linked list. if there's not, it's over complicated.
        - The solution is to create a dummy node and point it to head.
    - Example: 1->2->3->4->5, n=2
        - Move right pointer n steps:
            - r at 1. n=2, move r to the right.
            - r at 2. n=1, move r to the right.
            - r at 3. n=0, stop.
        - Let l=head=1, pre=dummy
            - r at 3, move pre to 1, move l to 2.
            - r at 4, move pre to 2, move l to 3.
            - r at 5, move pre to 3, move l to 4.
            - r at None, stop. 
        - l is now at 4, which is the 2nd to the right of the linked list and that is the node we want to delete. Now we also keep track of pre, which is the node right before left. We can do pre.next = pre.next.next (skip left).
        - Then return dummy.next (can be head, or can be null).

### Pseudocode
- Create dummy node. dummy.next = head
- Assign r = head
- while i in range of n, r = r.next
- pre = dummy, l = head
- While r:
    - pre = l
    - l = l.next
    - r = r.next
- pre.next = pre.next.next
- return dummy.next

### BigO
- Go through the linked list exactly 1 time => O(N).
- Space O(1).


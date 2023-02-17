### Question
[Link to question.](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

### Thoughts
- Input and output:
    - Input: 2 linked lists, represent long non-negative numbers in reverse order.
    - Output: a linked list, represent the sum of the 2 numbers, also in reverse order.
- Questions:
    - Can we assume there's no trailing 0s? yes.
    - Can the 2 linked lists have different length? yes.
- It's pretty straightforward that we will move the pointer at 2 linked lists at the same time from the beginning, take the sum of those 2 numbers.
- Edge case is when there's a carry. So we have to check to see if there's carry at each round. If there is, plus the carry with the total before determining the digit.
- Another thing that makes the problem simpler is to make a dummy head. So when we return the list, we can just return dummy.next (the real head).
- Example: 2->4->3, 5->6->4
    - Initialize dummy head value 0, cur = dummy. p1=l1, p2=l2. carry= 0
    - p1=2, p2 = 5. total = p1+p2+carry = 2+5+0 = 7. cur.next.val=7%10=7. Since total is not >= 10 then carry stays 0. cur = cur.next
    - p1=4, p2 = 6. total = p1+p2+carry = 4+6+0 = 10. cur.next.val=10%10=0. Since total is >= 10 then carry becomes 1. cur = cur.next
    - p1=3, p2 = 4. total = p1+p2+carry = 3+4+1 = 8. cur.next.val=8%10=8. Since total is not >= 10 then carry becomes 0. cur = cur.next
    - carry = 0, p1 None p2 None.
    - Return dummy.next: 7->0->8.

### Pseudocode
- Initialize variables: 
    - dummy = ListNode(0)
    - p1,p2 = l1,l2
    - carry = 0
- When p1 and p2 are not None:
    - Calculate total = p1.val + p2.val + carry
    - cur.next = Node(total%10)
    - if total > 9 then carry = 1 else 0.
- When either p1 or p2 is None
    - while p1 is still not None: do the same operation.
    - while p2 is still not None: do the same operation.
- If carry is still 1, create the last node and assign it to carry.
- Return dummy.next

### BigO
- Go through each list exactly once, so runtime O(N+M).


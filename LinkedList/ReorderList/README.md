### Question
[Link to question.](https://leetcode.com/problems/reorder-list/)

### Thoughts
- Input and output:
    - Input: a linked list. `L0 → L1 → … → Ln - 1 → Ln`
    - Output: the list after being reordered (return nothing since we change the list in place). `L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`
- Brute force: count the number of nodes in the linked list. Then from current node moved to the appropriate end node (potential next node), connect them together, recalculate the steps and continue until 2 nodes in the middle meet each other.
- My approach: O(N) time, O(N) space
    - Go through the list to count the number of nodes and find the half point (count/2), at the same time add them into a stack of node. So the top of the stack would be the last node, the 2nd to the top is the (n-2)th node etc.
    - Start from the beginning, pop the top node out of the stack, connect the current node with the node we just popped, move on to the next one. Do that `half` times.
    - Update the last node next pointer to None.
- The smart dude approach: O(N) time, O(1) space.
    - Have 2 pointers, 1 go 1 at a time, 1 go 2 at the time to find the middle node.
    - Reverse the second half of the list.
    - Go through the 2 halves, connect the 1st node of each half to each other.

### Pseudocode
#### My approach
- Go through the list and count the number of nodes to get half.
- Append all nodes to nodes []
- Go through half of the linked list:
    - Pop a node out of the list
    - Update cur node to connect to the popped node, popped node next is cur.next
- Update cur.next to None (the end node)

#### Smart approach
- Assign a fast and slow pointer
- Loop to find middle node
- Reverse the 2nd half of the linked list.
- Go through 2 halves and connect the nodes to each other.

### BigO
Mentioned above.



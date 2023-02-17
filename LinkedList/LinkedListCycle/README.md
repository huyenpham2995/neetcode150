### Question
[Link to question.](https://leetcode.com/problems/linked-list-cycle/description/)

### Thoughts
- Input and output:
    - Input: a linked list.
    - Output: boolean, either there's a cycle in the linked list.
- The linked list might have duplicate value at different nodes, so we can not use value to determine if we reach a cycle.
- Floyd's Tortoise and Hare
    - Have 1 slow pointer going 1 step at a time, a fast pointer moving 2 steps at a time.
    - if there's a cycle, fast pointer will meet slow pointer at a certain point of the linked list.
    - Why is that true?
        - Let's say the distance between fast and slow pointer is n.
        - slow pointer move 1 steps at a time, so when it moves, the distance between them is n+1.
        - But the fast pointer moves 2 steps at a time at that same time, so the distance between them is n+1-2 = n-1.
        - At each round, the distance will decrease (n-1) + 1 - 2 = n - 2, next time n-3 so on and so forth, until it reaches 0.
        - So it takes roughly O(N) time for them to meet each other.

### Pseudocode
- if head is None return False (empty linked list has no cycle).
- Initialize variables:
    - slow, fast = head, head
- While fast and fast.next:
    - Move slow 1 step.
    - Move fast 2 steps.
    - If fast and slow are the same then return True.
- If we reach the end of the linked list, that means there's no cycle. Return false.

### BigO
- O(N).

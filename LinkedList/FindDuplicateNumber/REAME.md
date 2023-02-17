### Question
[Link to question.](https://leetcode.com/problems/find-the-duplicate-number/)

### Thoughts
- Input and output:
    - Input: an array of n+1 number, the number ranges from 1->n.
    - Output: the duplicate number in this array.
- Approach 1 (violation): we can sort this array and check to see if 2 intergers next to each other are equal. This will take O(N) time and O(1) space, but the prompt does not allow us to modify the array.
- Approach 2 (violation again): go through the array and save the value in a dictionary that keeps count of each number. When a number has count > 1, return that number. That will take O(N) time and O(N) space, but we can only use O(1) space.
- Approach 3: At each number, traverse through the array to see if there's a duplicate. Return if there is. O(N^2).
- The correct approach: Floyd's algorithm.
    - First of all we need to createea linked list from the index of the elements, not the elements in the array itself.
        - Example: [1,3,4,2,2], index [0,1,2,3,4]. 
            - So index 0 connect to index 1 (beacauyse nums[0] = 1), meaning index 0 connect to nums[1] = 3. 
            - At nums[1]=2, meaning 3 connect to nums[3]=2. 
            - At nums[2]=4, meaning 2 connct to nums[4]=2.
            - So we have 0->3(nums[1])->2(nums[3])->4(nums[2])->2(nums[4])->4(nums[2])->...
            - The cycle is 2.
    - The concept behind this is that, we have a slow pointer and fast pointer, 1 going 1 step at a time, the 2nd going 2 steps at a time. If there's a cycle, they will meet each other at some point inside the cycle. Call M the point they meet, A the beginning of the cycle. The distance between M and A is the same as the distance between the beginning of the linked list to A. So if we have the 2nd slow pointer that going 1 step starting at the beginning of the linked list, then continue to move the first slow pointer, slo1 and slow2 will meet at the beginning of the cycle, i.e the duplicate number. 
    - This will work because there's n+1 number in the array, so the largest index is n, also the numbers run from [1...n] so we never get index out of range.
    - This is the type of problenm that you either know this algorithm, remember it to solve questions or you just cannot solve it with the constraint (which I don't like).


### Pseudocode
- slow1, fast: all start at the beginning (index 0).
- while True:
    - move slow 1 at a time: slow = nums[slow]
    - move fast 2 at a time: fast = nums[nums[fast]]
    - if slow==fast: break
- slow2=0
- while True:
    - slow = nums[slow]
    - slow2 = nums[slow2]
    - if slow==slow2:
        return slow

### BigO
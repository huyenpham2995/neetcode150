### Question
- Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
- You must implement a solution with O(1) time complexity for each function.
- [Link to question.](https://leetcode.com/problems/min-stack/)

### Thoughts
- Everything about this question is straight forward, except for getting min element in constant time.
- The trick here is to store the minimum number in a stack, and add the current minimum number to the stack every time a number is pushed in the main stack.
- Example: push 0, 1, 3, -1, 4. in the stack.
    - At first, the min_stack = []
    - When we push 0 to the stack, also append 0 to the min_stack = [0].
    - Now come 1. Is 1 smaller than the top of min_stack? No. So min number stays 0. Add another 0 to min_stack [0,0].
    - Now come 3. Is 3 smaller than the top of min_stack? No. So min number stays 0. Add another 0 to min_stack [0,0,0].
    - Now come -1. Is -1 smaller than the top of min_stack? Yes. So min number is -1. Add -1 to min_stack [0,0,0,-1].
    - Now come 4. Is 4 smaller than the top of min_stack? No. So min number stays -1. Add another -1 to min_stack [0,0,0,-1,-1].
- The min_stack has the same amount of numbers as the main stack. So if we pop a number out of the main stack, we also pop the top number out of the min_stack and still can keep track of the element. Since we only pop the top of the stack, there's no way the min number is popped out of the min_stack before it is out of the main stack.
- This method is smart, because if the min number is popped out of the stack and we only keep a single variable as the min number, that min number will need O(N) time to be updated.

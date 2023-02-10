### Question
[Link to question.](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

### Thoughts
- Input and output:
    - Input: list of heights of each retangle.
    - Output: the area of the largest rectangle that can be created.
- Naive approach: Go through each height, at each position calculate the area of all the rectangle that can be created there and save the max area.
- Better approach:
    - If there are 2 bars and the first one is higher than the second one, the first one cannot stretch further because of the height of the second one. But if the 1st one is lower, then it can be stretched out to the 2nd bar.
        - Example: [2,1,2]
            - At height = 2, the area is 2.
            - At height = 1, there are 2 areas that can be calculated: the are at position 1 (which is 1), and the area of height 1 stretches back at position 0 (2* = 2).
    - Knowing that, we can have a stack (height, position) to keep track of the bar in ascending order. Once we encouunter a bar that is lower than the previous bar, we start to pop the higher bar out of the stack and calculate max area, until we hit a less or equal bar again.
    - Since the lower bar can stretch backwards, we replace the index of the current position to the index of the previous position that was popped out of the stack.
    - An edge case would be that the last bar is the highest bar, so when we reach it we might miss calculating the area for it. A fix would be to add an additional 0 at the end of the heights array. Nothing can be lower than 0 so we will definitely calculate the last bar.
    - Example: [2,1,5,6,2,3]:
        - At 0 at the end. height becomes [2,1,5,6,2,3,0]
        - At position 0, height = 2. Stack is empty, append (2,1) to stack. stack = [(2,0)]. max_area = 0
        - At position 1, height = 1 < 2? yes. Pop (2,1) out of stack. area = height[1]*(1-stack[-1][1]) = 2*(1-0) = 2. max_area = 2. Take index of (2,0) which is 0 and append (height[1], taken_index) = (1,0) to stack. stack = [(1,0)].
        - At position 2, height = 5 < 1? No. Just append (5,2) to stack. stack = [(1,0),(5,2)].
        - At position 3. height = 6 < 5? No. Just append (6,3) to stack. stack = [(1,0),(5,2),(6,3)].
        - At position 4, height = 2 < 6? yes. Pop (6,3) out of stack. area = height*(4-stack[-1][1]) = 6*(4-3) = 6. max_area = 6. stack = [(1,0),(5,2)].
            - Go back if the stack is not empty. height = 2 < 5? Yes. Pop (5,2) out of the stack. area = height*(4-stack[-1][1]) = 5*(4-2) = 10. max_area = 10. stack = [(1,0)]
            - Go back if the stack is not empty. height = 2 < 1? No. Just push (2,taken_index) = (2,2) to the stack. stack = [(1,0),(2,2)].
        - At position 5, height = 3 < 2? No. Just append (3,5) to stack. stack = [(1,0),(2,2),(3,5)].
        - At position 6, height = 0 < 3? yes. Pop (3,5) out of stack. area = height*(6-stack[-1][1]) = 3*(6-5) = 3. max_area = 10. stack = [(1,0),(2,2)].
            - Go back if the stack is not empty. height = 0 < 2? Yes. Pop (2,2) out of the stack. area = 2*(6-stack[-1][1]) = 2*(6-2) = 8. max_area = 10. stack = [(1,0)]
            - Go back if the stack is not empty. height = 0 < 1? Yes. Pop (1,0) out of the stack. area = 1*(6-stack[-1][1]) = 1*(6-0) = 6. max_area = 10. Push(0,0) to stack. stack = [(0,0)].
        - End of loop.

### Pseudocode
- If list is empty, return 0.
- Append 0 to the last of height list.
- stack = [] #(height, index)
- Go through all elements in list:
    - Taken_index = current_index
    - while stack is not empty and current height < top of stack height:
        - height, taken_index = Pop top out of list
        - calculate area = current_height*(current_index - taken_index).
        - Reassign max_area if needed
    - Append(current_height, taken_index)
- Return max_area

### BigO
- Go through each elements at most twice => O(N) runtime.

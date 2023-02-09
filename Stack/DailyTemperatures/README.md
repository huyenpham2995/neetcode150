### Question
- Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
- [Link to question.](https://leetcode.com/problems/daily-temperatures/description/)

### Thoughts
- Input and output:
    - Input: list of temperatures for each day.
    - Output: a list of the number of days you have to wait.
- Brute force solution: at each day, go through the list from the i+1 position to a position where the temperature is higher than the current temperature. If reaching the end of list, then put a 0 in the ith position of the result. This method will take N^2 time.
- Better solution:
    - Use a stack to keep track of the temperature and its day.
    - Keep putting the (index, temperature) into the stack until we hit a temperature that is higher than the top temperature.
    - Calculate the day we need to wait, which is (i at current position - i of the top of the stack).
    - Example: [30,60,90]
        - The stack is empty, so push (0, 30) to it.
        - Next come (1, 60). Peek at the top of the stack. is 60 > 30? Yes, pop 30 out, result = 1-0 = 1. Push (1, 60) to stack.
        - Next come (2, 90). Peek at the top of the stack. is 90 > 60? Yes, pop 50 out, result = 2-1 = 1. Push (1, 90) to stack.
        - End of list. Return [1,1,0] as result.
    - Example: [75,71,69,72]
        - The stack is empty, so push (0, 75) to it. Stack = [(0,75)]
        - Next come (1, 71). Peek at the top of the stack. is 71 > 75? No. Just push (1, 71) to stack. Stack = [(0,75),(1,71)]
        - Next come (2, 69). Peek at the top of the stack. is 69 > 71? No. Just push (2, 69) to stack. Stack = [(0,75),(1,71),(2,69)]
        - Next come (3, 72). Peek at the top of the stack. is 72 > 69? Yes. Pop (2,69) out, result[2]=3-2=1. 
            - Is 72 > 71? Yes. Pop (1,71) out, result[1]=3-1=2. 
            - Is 72 > 75? No. Push (3, 72) to stack. Stack = [(0,75),(3,72)].
        - End of list. Return [0,2,1,0] as result.

### Pseudocode
- Initialize variables:
    - stack = []
    - result = [0*len(temperatures)]
- Go through all elements in temperatures:
    - while the list is not empty or the current temperature is larger than the top of the stack
        - pop the top out of the stack (a pair of (index, temp))
        - Calculate result[i] = i - index
    - Append current temp to stack.
- Return result

### BigO
- Go through each element once => O(N) runtime.



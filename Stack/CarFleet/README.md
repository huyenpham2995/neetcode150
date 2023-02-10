### Question
[Link to question.](https://leetcode.com/problems/daily-temperatures/description/)

### Thoughts
- Input and output:
    - Input: 
        - position array: the initial position of each car.
        - speed array: the speed of each car.
    - Output: an int (number of carfleets).
- Brute force: for ith car, go through all the cars after that and check to see if it makes a car fleet. Add them to a dictionary with the key being (p,s) of each car. Return the length of the dictionary at the end. This approach takes O(N^2) time.
- Better approach:
    - If we sort the cars by their distance, we get a car that is closest to the target.
    - We calculate the time it takes for it to take to the target ((target-p)/s)
    - If there's a car afterwards that takes a shorter time to get to the target, we know that the first car and that car will meet somewhere in the middle of the road.
    - If the car afterwards cannot catch up to the first car, we know the carfleet "streak" ends. Why?
        - When a car catches up to another one in front of it, it will run at the same speed as the one in the front.
        - So any cars start off behind have no way to pass the car in the front.
    - Can just keep a stack of the time it takes for a car to get to the target.
        - If the car after has shorter time, don't add it to the stack.
        - If it takes more time for the car after, add that time to the stack.

### Pseudocode
- Check if the list only has 1 element. If so return 1 (1 car = 1 fleet)
- Create a list of zip(position, speed).
- Sort the list in reverse position order (from large to small).
- Initialize stack = []
- Go through the sorted list.
    - Calculate time to target = (p-target)/s
    - If the list is empty or time to target > the top of the stack: add that time to target to the stack.
- At the end, return the length of stack.

### BigO
- Sort the list takes O(NlogN), go through the list 1 time takes O(N) => O(NlogN) runtime.

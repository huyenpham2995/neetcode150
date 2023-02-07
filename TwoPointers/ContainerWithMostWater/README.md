### Question
- You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
- Find two lines that together with the x-axis form a container, such that the container contains the most water.
- Return the maximum amount of water a container can store.
- Notice that you may not slant the container.
- [Link to question.](https://leetcode.com/problems/container-with-most-water/)

### Thoughts
- Input and output:
    - Input: an array of lines' height.
    - Output: the maximum area of the container.
- My original thought (and it's wrong):
    - Having 2 pointers, 1 at the beginning (l) 1 at the end(r).
    - The difference in distance between those 2 pointers is the width.
    - The minimum numbers out of the 2 numbers at height[l] and height[r] is the height of the container at position l and r.
    - I will calculate the area of the current position, the area to the "left" (moving r pointer to the left), the area to the right (moving l to the right) and take the maximum area out of the 2, then move l to the right and r to the left for next calculation.
    - This comes as a mistake, since if the maximum area is something at is not in the area of (l, r), (l+1, r), (l, r-1), then it will not be captured.
- The fix:
    - By putting the 2 pointers at the 2 ends, that's the position of the maximum height. The closer we move those 2 pointers, the width will become smaller. That's when we need to maximum the height.
    - How to maximum height?
        - Start by moving l pointer. Take min(height[l], height[r]) and calculate the area. If the area is bigger than the current area, update max area.
        - We want that min to be as high as possible, so the "lower end" between the 2 heights need to be the highest.
            - If the height at l is lower than the height at r, we are on an adventure to try and find something bigger than the height at r (if possible). Move l.
            - Vice versa, move r if height at r is lower than height at l.
            - Each time we move, we calculate the area and see if we can update the area.
            - This will stop when l meets r (width = 0).
    
### Pseudocode
- If the length of the height array is 1 or 0, return 0 (cannot create a container).
- Initialize variables:
    - l starts at 0, r starts at the end (len(height) - 1)
    - max_height = 0
- When l < r:
    - Calculate the area between l and r.
        - If it's > max_area, update max_area.
    - If height at l is < height at r, move l up.
    - If height at r is < heihtat l, move r down.
- Return max_height.

### BigO
- With 2 pointers, space capacity is O(1).
- We go through the array exactly 1 time with 2 pointers => O(N) runtime.



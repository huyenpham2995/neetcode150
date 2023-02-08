### Question
- Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
- [Link to question.](https://leetcode.com/problems/trapping-rain-water/)

### Thoughts
- Input and output:
    - Input: an array of elevation height.
    - Output: the maximum area of the container.
- My original thought (and it's wrong):
    - Having 2 pointers:
        - 1 on the left keep track of the high wall.
        - The right one keeps moving until hitting the higher wall than p1.
        - Each time p2 moves, calculate the block area.
        - When hitting a higher wall, calculate the "total area".
        - At the end, take the total area - block area = water trapped.
    - This solution will work if eventually the wall on the right is higher than the one on the left, but if at the end, the wall on the left is higher then it will miss the whole portion on the right.
- After taking hints:
    - Still having 2 pointers, 1 at the beginning and 1 at the end. will move depends on which one has a higher value.
    - The point is, at the position i, find the max height on the left, the max height on the right, take the min of them to find the "container" that can trap water at that position.
        - Example: left_max = 2, right_max = 3, the highest wall that can trap water in is min(left_max, right_max) = 2. Let's say the high of the current position is 1, then we can trap 1 unit of water if the wall height is 2.
    - The idea: take the h = min(height[l], height[r]), that's the maximum "wall" that can trap water inside. Then to calculate the water that we can trap at the current spot, take h - height[i].
    - We will consider the local min value at that spot and update the min accordingly.
    - Example: [4,2,0,3,2,5]
        - max_left = height[0] = 4
        - max_right = height[5] = 5
        - l = 0, r = 5.
            - height[l] = 4 = max_left, height[r] = 5 = max_right
            - Since max_left < max_right, calculate the water trapped at height[l]
            - wall = min(left_max, right_max) = 4. Water can trap: wall - height[l] = 4 - 4 = 0 => trap 0 water.
            - l += 1 = 1
        - l=1, r=5.
            - height[l] = 2 < max_left , height[r] = 5 = max_right
            - Since max_left < max_right, calculate the water trapped at height[l]
            - wall = min(left_max, right_max) = 4. Water can trap: wall - height[l] = 4 - 2 = 2 => trap 0+2=2 water.
            - l += 1 = 2
        - l=2, r=5
            - height[l] = 0 < max_left , height[r] = 5 = max_right
            - Since max_left < max_right, calculate the water trapped at height[l]
            - wall = min(left_max, right_max) = 4. Water can trap: wall - height[l] = 4 - 0 = 4 => trap 2+4=6 water.
            - l += 1 = 3
        - l=3, r=5
            - height[l] = 3 < max_left , height[r] = 5 = max_right
            - Since max_left < max_right, calculate the water trapped at height[l]
            - wall = min(left_max, right_max) = 4. Water can trap: wall - height[l] = 4 - 3 = 1 => trap 6+1=7 water.
            - l += 1 = 4
        - l=4, r=5
            - height[l] = 2 < max_left , height[r] = 5 = max_right
            - Since max_left < max_right, calculate the water trapped at height[l]
            - wall = min(left_max, right_max) = 4. Water can trap: wall - height[l] = 4 - 2 = 2 => trap 7+2=9 water.
            - l += 1 = 5
        - l=r=5 stop.
        - Return 9
    
### Pseudocode
- If list is empty, return 0.
- Initialize variables:
    - l, r = 0, len(height)-1
    - max_left, max_right = height[l], height[r]
    - water_trap = 0
- while l <= r:
    - trap = 0
    - If max_left <= max_right: 
        - trap = min(max_left, max_right) - height[l]
        - if height[l] > max_left => max_left = height[l]
        - l += 1
    - else:
        - trap = min(max_left, max_right) - height[r]
        - if height[r] > max_right => max_right = height[r]
        - r -= 1
    - water_trap += trap if trap > 0
- Return water_trap

### BigO
- With 2 pointers to keep track of, space complexity is O(N)
- Go through the array 1 time => runtime O(N)



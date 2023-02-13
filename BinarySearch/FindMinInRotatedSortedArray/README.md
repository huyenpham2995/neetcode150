### Question
[Link to question.](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

### Thoughts
- Input and output:
    - Input: a rotated sorted array.
    - Output: the min value of that array
- Since the array can be rotated n times, there are multiple scenerio that can happen:
    - The min number at the beginning.
    - The min number is somewhere in the middle of the array.
    - The min number is at the end of the array (after array rotating n-1 times).
- My thought trap: 
    - Compare the mid element to the next element. If the next one is smaller, then that next one is the min.
    - If the min is at the beginning of the array (index 0)
        - Compare that one to the next one and the one at the last of the array. If that's the min then return nums[0].
        - If the min is at the last of the array, move left and right bounds to the later half of the array and run the algorithm again.
- What is more efficient? 
    - Instead of comparing to THE NEXT element, compare the mid element to THE LAST element of the array.
        - If the last element is bigger, then we know min is lying at the first half of the array. There's no way it's on the right side of mid, since the end is bigger than mid, from mid -> end will contain all numbers that are larger to mid.
        - If the last element is smaller, i.e the array has been rotated, then the min is somewhere in the later half of the array. Move left and right bounds to the right, computing mid, keep track of min.
        - Return min.
- Example: [4,5,6,7,0,1,2]
    - l=0, r=6. mid = 3, min=inf. nums[3] = 7 < inf => min = 7. Compare 7 to the end of the array. 7 > 2 => min is somewhere at the 2nd half. Update l = mid+1 = 4, r=6.
    - l=4, r=6. mid= 5. nums[5] = 1 < 7 => min=1. Compares 1 to the end of the array. 1<2 => min is somewhere at the "first half". update l=4, r=mid-1=4.
    - l=4, r=4. mid=4. nums[4] = 0 < 1. min = 0. Compare 0 to the end of the array. 0<2 => min is somewhere at the first half. update l=4, r=mid-1=3.
    - l=4 > r=3, loop stop, return min=0.

### BigO
- Basically binary search O(logN).
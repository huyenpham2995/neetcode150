### Question
-[Link to question.](https://leetcode.com/problems/search-in-rotated-sorted-array/)

### Thoughts
- Input and output:
    - Input: 
        - array of int, sorted, rotated.
        - A target.
    - Output: the index of the target.
- Since the array is rotated, the numbers are not in order. But either on the left side or the right side, they will be sorted.
    - Example: [7,0,1,2,3]. The pivots is 0. On the right side of 1 it is sorted, the left side is not.
    - [4,5,6,0]. Left side is sorted, right side is not.
- Approach: using binary search to find the middle. depends on the mid, left and right number to determine which side is sorted and where to go, until either find the target or left > right. 
    - If left side is sorted, that means mid number is larger than the far left number (ascending order from left to middle), then the right side is not sorted. If we need a number that is smaller than mid and larger than left, go left. Else go right.
    - If right side is sorted, that means mid number is smaller than the far right number (ascending order from mid to right), then the left side is not sorted. If we need a number that is bigger than target and small than right, go right. Else go left.
- Example: [7,0,1,2,3]. Find 7.
    - l=0, r=4. mid=2. nums[2] = 1 < target=7. nums[l]=7 > [mid], then right side is sorted. 7 is larger than [mid] but also larger than [r] = 3, then we go left.
    - l=0, r=1. mid=0. nums[0] =7 == target. Return mid=0.

### Pseudocode
- If list is [] return False.
- Initialize variables:
    - l=0, r=len(nums)-1.
- While l <= r:
    - mid = (l+r)//2
    - if [mid] == target: return mid
    - if the left side is sorted (i.e [l] < [mid]):
        - if target < [mid] and target > [l]: go left
        - else go right.
    - If the right side is sorted (i.e [mid] < [r]):
        - if target > [mid] and target < [r]: go right
        - else go left.
- if we reach this part, which means we cannot find target in the list, return -1.

### BigO
- Binary search method, takes O(logN).

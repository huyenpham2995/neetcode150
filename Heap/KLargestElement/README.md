### Question
- [Link to question.](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

### Thoughts
- Input and output:
    - Input: 
        - Array of numbers (have at least 1 elements).
        - Integer k, represent the kth largest element (1 < k < number of elements in the array).
    - Output: the k largest element in the array.
- Approach 1: sort the array and find the kth largest element. We can sort the array in NlogN time and finding the kth largest in O(1) time (the index of kth largest element is len(nums)-k).
- Approach 2: heap. We create a max heap out of the array. Since we have all the elements upfront and we use heapify, creating a heap takes O(N) time. After that, we pop out of the heap k time. Each pop takes O(logN) times (because we need to reheap up/down), so this operation takes O(klogN) time, slightly better than the previous approach.
- Approach 3 (which takes on AVERAGE O(N) time, but in worst case it will be O(N^2)): Quick select.
    - Quick select idea: pretty similar to quick sort, but we don't work on both sides of the array, just one side (search, instead of sort).
    - The idea is to choose the last element as the pivot. We move all the elements < pivot to the left, and all elements > pivot to the right. The position of the kth largest element is len(nums) - k. So if the pivot is at position len(nums) - k (calling it p), it is the one that we are looking for.
        - Why? Because we know that if pivot is at len(nums) - k position, there are exactly k numbers that are larger than the pivot.
    - How?
        - Having a p pointer to track the mid point (the point that divde half < pivot, half > pivot).
        - Choose a pivot, i.e the last element in the array range that we consider.
        - Going through the array from start to end, excluding the last element (since it is the pivot). If the curret position (i) of the array < pivot, switch the position between p and i, then move p up.
        - At this time, p is at the line that separte all elements that are smaller and larger then pivot. Switch p and pivot so that pivot stay right in the middle. 
        - If p == len(nums) - k, this pivot is the number we are looking for.
        - If p < len(nums) - k, that means the number we are looking for has to be bigger than this current pivot, so we will continue this search on the right side of the array, starting from p+1 to the end.
        - On the other hand, if p > len(nums) - k, that means the result is less than the current pivot, we continue the search on the left side, starting from start to p-1.
    - Example: nums = [3,2,1,5,6,4], k = 2
        - We go through the array from start = 0, end = len(nums) -1 = 5. p = start = 0, pivot = 4:
            - i=0, 3 < pivot, so switch p and i (switch with itself), then p += 1 = 1.
            - i=1, 2 < pivot, so switch p and i (switch with itself), then p += 1 = 2.
            - i=2, 1 < pivot, so switch p and i (switch with itself), then p += 1 = 3.
            - i=3, 5 > pivot, keep going.
            - i=4, 6 > pivot, keep going.
            - Reaches the end of loop.
        - Switch the number at position p=3 (5) and the last element (4), array becomes [3,2,1,4,6,5]
        - p = 3 < len(nums) - k = 6-2 = 4, so we know we have to search on the right side of the array.
        - We go through the array from start = p+1 = 4, end = 5. p = start = 4, pivot = 5:
            - i = 4, 6 > pivot so move on.
            - End of loop.
        - Switch the number at position p=4 (6) and the last one (5), array becomes [3,2,1,4,5,6]
        - p = 4 == len(nums) - k = 6-2 = 4, so we return nums[4] = 5 as the kth largest element.

### Pseudocode
- Create a helper function for recursive use called helper.
    - nums
    - k
    - start position: 0
    - end position: len(nums) - 1
- In helper function
    - if the start >= end, then return nums[end].
    - Initialize p = start, pivot = nums[end].
    - Go through the loop from start to end:
        - if the current number < pivot:
            - switch current number with number at position p.
            - p += 1
    - Switch the number at position p with the number at the end (pivot).
    - Check p:
        - If p == len(nums) - k, return nums[p] // found kth largest element.
        - If p < len(nums) - k, call helper with start = p+1, keep the end.
        - If p > len(nums) - k, call helper with end = p-1, keep the start.

### BigO
- O(N) on average case, O(N^2) worst case (if the pivot is the largest/smallest element in the array).

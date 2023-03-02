### Question
- [Link to question.](https://leetcode.com/problems/k-closest-points-to-origin/description/)

### Thoughts
- Input and output:
    - Input: the list of points ([x,y] represents their coordination).
    - Output: the list of K closest points to the origin (0,0).
- We can solve this problem using min heap.
    - Go through the list once and calculate the distance (theoretically need to find the square root of (x-0)^2 + (y-0)^2, but for simplicity just need to calculate x^2 + y^2.
    - Push the element into the min heap using the form of [distance,x,y].
    - By default, min heap will be calculated by distance.
    - While the result list has not had k elements:
        - Pop from min heap (the element we pop is the smallest element in the min heap, aka the one with the smallest distance).
        - append [x,y] to the result list.
    - Return the result list with k elements.
    - Trick: if k > the number of points, when the min_heap becomes empty we return the result list, don't need to to wait for the result list to have k elements because it never will.

### BigO
- Building min heap: O(NlogN), but if we know all the element from the beginning it should be O(N).
- Popping k times O(KlogN).
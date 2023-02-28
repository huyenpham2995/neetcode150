### Question
- [Link to question.](https://leetcode.com/problems/last-stone-weight/description/)

### Thoughts
- Input and output:
    - Input: the stone weights.
    - Output: the last stone weight.
- If there is only 1 stone in the list, return the weight of that stone.
- Since we need to compete 2 heaviest stone together, we can sort the list and take 2 first elements out of the list to compete. But it will take time to put the difference back into the list (basically putting back the element into a sorted list again).
- We can ultilize heap for this.
- Using a max heap. Each time we will pop out 2 elements from the heap (first one will be y, second one is x because x<=y by assumption).
- If y > x, calculate y-x and push that back into the heap.
- keep doing that until the heap has at most 1 element left.
- Trick to keep in mind:
    - The built in heapq library of python only create min heap by default. To get max heap, multiply all of the weights in the array with -1 (flip). Then the root of the min heap will actually the weight of the heaviest stone.

### BigO
- O(NlogN) for creating the heap.
- O(1) for popping out 2 elements.
- O(logN) for adding y-x back to the heap.
- So overall O(NlogN).

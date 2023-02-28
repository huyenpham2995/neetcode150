### Question
- [Link to question.](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)

### Thoughts
- We are given an array in the beginning (a stream), but the only functionality we really need to implement is to add a new element into this stream and find the Kth largest element.
- We don't really need to keep all of the element in this list. Instead, we can just keep track from the Kth largest element to the last one.
- How to do that?
    - When we were given the initial list, build a min heap from there (using Python built in heapq library), by default heapify provides min heap.
    - From then, if the list has more than K elements, we pop the element out until it only has k elements. Why?
        - The element we pop out from the heap each time is the smallest element of the current list.
        - By popping elements out until we are left with k elements, we ensure the next out we pop out will be the Kth largest element in the list.
        - If the list does not have K elements, then the smallest one will the be Kth largest (i.e we don't pop anything out).
    - For add functionality:
        - First of all add the new value to the list. Using heappush will make sure the value is added to the right position in the heap.
        - Since we will have maximum K elements in the list (we pop out all elements and leave k left in the init step), adding this value means we have at most (k+1) elements in the heap.
        - Check to see if we have more than K elements in the heap, if yes, pop 1 out (now we have k elements).
        - Return the root of this heap (which will be the Kth largest elements).

### BigO
- Getting Kth largest takes O(1) time (only pop the root).
- Adding element to the heap takes O(logn) (heapify).
- Popping elements out of the heap takes at most N times (imagine k being 1).

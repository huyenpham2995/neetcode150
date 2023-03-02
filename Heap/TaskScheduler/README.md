### Question
- [Link to question.](https://leetcode.com/problems/task-scheduler/description/)

### Thoughts
- Input and output:
    - Input: 
        - Array of tasks.
        - Integer n, the cool down time.
    - Output: the shortest time it takes to finish all the tasks.
- In a special case, if n=0 meaning there's no cooldown time, the time to complete the tasks will just be the number of tasks available in the array. Or if there's only 1 task that needs to be scheduled, then retunr 1.
- Strange thing happens when cooldown time involved.
- First we need to count how many time a task appears, because to do the same task again, it's best to do it when the cooldown time has passed.
    - if n=2, and we have task A, we have to either wait for 2 (unit of time) or do 2 other different tasks first before coming back to again.
- Once we have the list of all the unique tasks and their counts, and prefer to start with task that has the highest occurence first since we will reduce the cooldown time if we can "mix" this task with other in between.
    - Example: A,A,A,C, n=2. If we do C first, then the time it takes is C->A->wait->wait->A->wait->wait->A, T = 8. If we do A first: A->C->A->wait->wait->A, T=6.
- To achieve this, we need a max heap.
    - Each time we pop out the root of the max heap and process up to n nodes (since n is the amount of wait time if we have to process the same node again).
        - If we don't have enough n node, then we will add the idle time in to reach n.
        - Then we push all the nodes that have been process (and still need to be processed) back to the heap.
        - We continue until heap is empty.
    - Example: ["A","A","A","B","B","B"], n = 2.
        - Count each tasks, end in {A:3,B:3}.
        - Build a max heap based on this dictionary. t=0, i=0
        - Round 1: 
            - i=0: pop A:3 out of heap. t += 1 = 1. Reduce A count to A:2
            - i=1: pop B:3 out of heap. t += 1 = 2. Reduce B count to B:3
            - i=2, we have nothing in the heap to process
            - Adding back A:2, B:2 to the heap.
            - missing 1 idle time before we can process A again (n-i+1), so t += n-i+1 = 3.
        - Round 2: 
            - i=0: pop A:2 out of heap. t += 1 = 4. Reduce A count to A:1
            - i=1: pop B:2 out of heap. t += 1 = 5. Reduce B count to B:1
            - i=2, we have nothing in the heap to process
            - Adding back A:1, B:1 to the heap.
            - missing 1 idle time before we can process A again (n-i+1), so t += n-i+1 = 6.
        - Round 3:
            - i=0: pop A:1 out of heap. t += 1 = 7. Reduce A count to A:0
            - i=1: pop B:1 out of heap. t += 1 = 8. Reduce B count to B:0
            - i=2, we have nothing in the heap to process
            - Both A and B don't have any task left so we don't add any back to the heap.
            - Heap is empty, return t=8.

### Pseudocode
- If n==0 or len(tasks) < 1: return len(tasks)
- Create a dictionary, loop through the tasks to count the number of each tasks.
- Create a max heap (heapify the items in the dictionary with count*-1)
- time = 0
- While max_heap:
    - arr = []
    - i = 0
    - while i<=n:
        - Pop item out of heap
        - add 1 to count
        - add 1 to time t
        - append the task to arr if count < 0 (in absolute value there's still task left).
        - push back all the items in the array to the heap
        - Add the idle time (n-i+1) to t if i<=n and there's still task to do.
- return time t.

### BigO


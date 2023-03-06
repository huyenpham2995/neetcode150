### Question
- [Link to question.](https://leetcode.com/problems/subsets/description/)

### Thoughts
- Input and output:
    - Input: the list of all numbers.
    - Output: the list of all possible subsets.
- This is a tricky question since we have to exhaust all the possible solution at the current position before we can move on.
- At each location, we can determine if we want to take the item or not. The final result looks like a tree.
- Example: input = [1,2,3], output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]. How?
    - At 1, you can choose if you want to include 1 or not. If yes, list becomes [1]. No? List is []
    - At list [], decide if you want to include 2. Yes?, list becomes [2]. No? List stays []
    - At list [1], decide if you want to include 2. Yes?, list becomes [1,2]. No? List stays [1]
    - At list [], decide if you want to include 2. Yes?, list becomes [2]. No? List stays []
    - At list [1,2], decide if you want to include 3. Yes?, list becomes [1,2,3]. No? List stays [1,2]
    - At list [1], decide if you want to include 3. Yes?, list becomes [1,3]. No? List stays [1]
    - At list [2], decide if you want to include 3. Yes?, list becomes [2,3]. No? List stays [2]
    - At list [], decide if you want to include 3. Yes?, list becomes [3]. No? List stays []
    - At the end, you have the output.

### Pseudocode
- Initialize res = [] (keep track of the results), subset = [] (keep track of all elements currently in the subset).
- Design a helper function to help with the recursion, taking in an index.
    - if i>=len(nums), then append the current subset to result (nothing more to add since we reach the maximum number of nums that we can add to the subset).
    - Option 1: take the current number: 
        - append nums[i] to the subset. 
        - call helper again with i+1 to process the next item.
    - option 2: don't take the current number:
        - Pop the number out of the subset
        - call helper with i+1 to process the next item.
- In the main function, call helper with i=0.
- Return result.

### BigO
- Go through all the element in the array nums and create 2^N subsets => O(Nx2^N).

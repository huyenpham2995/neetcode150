### Question
[Link to question.](https://leetcode.com/problems/search-a-2d-matrix/description/)

### Thoughts
- Input and output:
    - Input: 
        - an mxn integer matrix.
        - A target (int).
    - Output: a boolean, true if target is in the matrix.
- Can flatten out the matrix. Since the first integer of each row is larger than the last integer of the previous row, if we flatten out the array it will be a sorted single array. Then apply binary search on the flatten array takes O(log(m+n)) time. But this takes extra memory (m+n space) to store the flatten array.
- The second way is to binary search to find the correct row, then apply binary search on that row:
    - Perform binary search on the first element of each row. 
    - If the target is there, cool, we found it without moving to the 2nd step.
    - If the beginning of that row is less than the target, but the end of that row is > target, that's the row we are looking for. If the end of that row is still smaller than target, move on to the next row.
    - If the beginning of that row is already > than the target, that's not the row we are looking for.
    - After finding out the row, search within that row using regular binary search on a single array.

### BigO
- Search for row takes log(m) (m is the number of rows).
- Search for the element within that row takes log(n) (n is the number of integers within that row).
=> O(logm + logn) = O(logmn).

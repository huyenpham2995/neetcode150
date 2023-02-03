### Question
- Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
- [Link to question.](https://leetcode.com/problems/top-k-frequent-elements/description/)

### Thoughts
- Input and output:
    - Input: 
        - A list of numbers.
        - Integer k for the number o
    - Output: a list k integer in nums that have the most frequency.
- Questions:
    - Can the array be empty? Yes, return empty result if so.
    - What if there are more than k numbers with the same frequency. Eg: [1,1,2,2,3,3,4], k = 2. The result can be [1,2], [1,2], [2,3]? In this problem, we assume there will only be exactly 1 answer.
- My first approach: need to keep count of the occurence of all numbers in the num list. Then sort it based on their count. Then take the top k numbers from the sorted list and return them.
    - It's easy to understand, but the question said: your runtime has to be better than O(nlogn). Sorting the list takes O(nlogn), so this answer is not what they are looking for.
- Another approach: using Max heap. Build a max heap out of the array, then just pop the root of the heap k times.
- Another approach (the most efficient one): BUCKET SORT.
    - There are N numbers in the list, so if we are to create an array listing the occurence of each number, it will take at most N slots (the case where all numbers appear 1 time).
    - With that knowledge, we first still go through the list one time and count the number of occurence for each number.
    - Then we create a bucket of N slots to store the counts and the number that has that counts. Example: [1,1,1,2,2,3]

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|[] |[3]|[2]|[1]|[] |[] |[] |

    - The index represents the frequency of seeing the numbers. The value at ith index is the list of numbers that appear i times in the list.
    - Then we go through this new created list but from the end (because the higher the index is, the larger the frequency), take the list at each index and append it to the result, until the result list reaches k numbers. Those will be the numbers we are looking for.

### Pseudocode
- If list is empty, return empty list.
- Initialize variables:
    - A dictionary with key as the unique numbers in the nums list, value is the count of the frequency of each number.
    - A result list.
    - A frequency array of size N where index represent the frequency, value at each index started off as empty list.
- Go through all numbers in num list, count their frequency and store them in the dictionary.
- Go through the dictionary:
    - For each pair of (num, frequency), go to the position i=frequency, insert num in the list of that slot.
- Go through the frequency array in reverse order (from the end to the beginning):
    - Append the value at each slot to result, until result has k element.
    - Return result.

### BigO
- Time complexity:
    - Go through the nums list to get count: O(N)
    - Go through the dictionary to insert to the frequency list: O(N)
    - Go through the frequency list to get the result list: O(N)
- Space complexity:
    - dictionary: O(N)
    - Frequency list: O(N)
    - Result list: O(N)


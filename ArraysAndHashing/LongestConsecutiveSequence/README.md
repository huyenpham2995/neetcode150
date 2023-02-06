### Question
- Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
- You must write an algorithm that runs in O(n) time.
- [Link to question.](https://leetcode.com/problems/longest-consecutive-sequence/)

### Thoughts
- Input and output:
    - Input: an unsorted array of integers.
    - Output: the length of the longest consecutive elements sequence.
- Questions:
    - If the array is empty, we return 0.
    - By defaut, if there's no consecutive sequence, the result is 1..
    - Will there be duplicate elements? Like [0,0,0,1,1,...]. Yes, in that case, `0,0,1` will have 2 longest cosecutive elements (0,1).
- The simplest way we can think of is to sort the array and count the consecutive numbers. But sorting takes O(nlogn) and this questions asks to be done in O(n) time.
- Optimization:
    - Add each of the number in a dictionary, with key as the number and value as the consecutive_count.
    - At each num, see if the number next to it (num+1) is in the dictionary (i.e) in the list as well. If it is, the consecutive_count of (num+1) will be the current consecutive count of (num+1) + the consecutive count of (num). 
    - Example: [100,4,200,1,3,2]
        - At first, all numbers has consecutive_count = 1. {100:1,4:1,200:1,1:1,3:1,2:1}.
        - Go through each of element and update their consecutive_count.
            - At 100, check to see if 101 is in the list. No, move on.
            - At 4, check to see if 5 is in the list. No, move on.
            - At 200, check to see if 201 is in the list. No, move on.
            - At 1, check to see if 2 is in the list. Yes
                - Update consecutive_count[2] += consecutive_count[1] = 1+1 = 2
            - At 3, check to see if 4 is in the list. Yes
                - Update consecutive_count[4] += consecutive_count[3] = 1+1 = 2
            - At 2, check to see if 3 is in the list. Yes
                - Update consecutive_count[3] += consecutive_count[2] = 1+2 = 3
            - End of list. Return 3.
    - BUT THIS IS THE WRONG ANSWER!! 
- True answer:
    - Go through the list and see if the number is the beginning of a sequence (i.e check to see if there's another number in front of it)
        - if there is, then it is not the beginning of a sequence, pass.
        - If none, see if Num+1 is in the sequence. And continue to count until the streak ends.
    - Example: [100,4,200,1,3,2]
        - Create a set of unique numbers in the list.
        - At 100, check if there's 99 in the list. None. This can be the beginning of a sequence
            - Check to see if 101 is there. Nope. max sequence remains 1
        - At 4, check to see if 3 is in the set. Yes, so it's not the beginning of a sequence. Pass.
        - At 200, check if there's 199 in the list. None. This can be the beginning of a sequence
            - Check to see if 201 is there. Nope. max sequence remains 1
        - At 1, check if there's 0 in the list. None. This can be the beginning of a sequence
            - Check to see if 2 is there. Yes Max sequence becomes 2.
            - Check to see if 3 is there. Yes Max sequence becomes 3.
            - Check to see if 4 is there. Yes Max sequence becomes 4.
            - Check to see if 5 is there. No, end max sequence at 4.
        - At 3, check to see if 2 is in the set. Yes, so it's not the beginning of a sequence. Pass.
        - At 2, check to see if 1 is in the set. Yes, so it's not the beginning of a sequence. Pass.
        - The end, return 4 as max_sequence.
    
### Pseudocode
- Return length of num list if len is < 1
    - If num list is empty, return 0.
    - If num list is 1, return 1.
- Initialize variables:
    - Set(nums)
    - Max_count = 1
- Loop through all numbers:
    - See if num-1 is in the set
        - if yes, it is not the beginning of a sequence. Pass
        - if no, countinng up until the streak end.
            - update max_count.
- Return max_count

### BigO
At most, when we find the beginning of a sequence and count up, we go through each element 2 times => O(2N) = O(N).



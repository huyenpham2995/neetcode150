### Question
-[Link to question.](https://leetcode.com/problems/time-based-key-value-store/)

### Thoughts
- Pretty straightforward. Asking to return the value with the closest timestamp to the given timestamp.
- Data structure used: dictionary
    - Key: key (string, given).
    - Value: tuple of (value, timestamp).
- To insert the key-value into the dictionary, just check to see if the key already existed. If it does, append the new value, if it's not, create a new key-value pair.
- To get the *closest* item to the given timestamp.
    - First retrieve the list of values for that key.
    - Use binary search to search for the item:
        - If the timestamp of mid is <= timestamp given, try to push it forward to find the *closest" one to the timestamp. 
        - When we have exhausted all the search (left pointer > right pointer), return the value of the maximum timestamp.

### BigO
- Binary search method, takes O(logN).

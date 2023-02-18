### Question
[Link to question.](https://leetcode.com/problems/lru-cache/description/)

### Thoughts
- Create a LRU cache:
    - When the cache reaches its limit, evict the least recently used item.
    - Have to insert into the cache in O(1) time, and get the value for a given key in O(1) time.
- We can store the key and value pair in a dictionary to retrieve the value in O(1) time, the more important thing is how to determine which key, value pair to evict in O(1) time?
- Use doubly linked list to log in the change:
    - The node structure:
        - key, value
        - Pointer to previous and next node
    - The cache structure:
        - A limit to store the capacity.
        - A dictionary to keep track of key value and retrieve them constant time
            - key is the key provided.
            - Value is a node.
        - A doubly linked list to keep track of the least recently used value.
            - it has 2 dummy nodes at the beginning and the end.
- How does the doubly linked list work?
    - The idea is to keep the least recently used value at the top left of the linked list (right after the dummy left node), and append the most recently used (recently inserted or accessed) at the very right (on the left of the dummy right node).
    - Each time we were told to put something in the linked list, check to see if that key is already existed in the dictionary. 
        - If it does not, create a new node with the given key and value, insert it into the doubly linked list, and set dict[key] = newly created node.
        - If it does, meaning they want to update the value of the key, then we first find the node by going to dict[key]. Then we remove that node from the linked list. Create a new node with the new key, value pair, insert it to the end of the linked list and update dict[key]. This way, this is the most recently used node and it is at the end, like we want.
        - Now we have to check if the cache exceed its capacity. If it is, find the node at the beginning of the linked list. We store key inside the node, so we can easily delete it from the dictionary. Then also remove that node from the linked list.
    - Each time we have a get request to a key, that key will be the most recently used. So we retrieve the node from dict[key], remove that node from the linked list and insert it again to the end of the linked list. Then we return the value. 
        - Even though the value does not change, we need to remove it from the linked list since we need to append it to the end of the linked list, indicate that's the most recently used block.
- With this method, we retrieve the value in constant time with the dictionary, retrieve the least recently used value in constant time since that block is always at the beginning of the linked list.

### BigO
- Put: O(1)
- Get O(1)

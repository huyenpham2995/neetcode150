### Question
[Link to question.](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

### Thoughts
- Input and output:
    - Input: a linked list.
        - val: the value of that node.
        - next: the next node it is pointing to.
        - random: a random node in the list that it is pointing to
    - Output: the deep copy of that linked list, none of the node should point to the original linked list.
- Pretty proud of my approach to use dictionary with key is the original node, value is the copy of that node.
    - If the list (i.e head is None) is empty then return None.
    - Starting from head, check to see if the current node is in the dictionary. If not, create it with the original node value.
    - Check to see if the node.next point to another node. If yes:
        - Check to see if that node already exists in the dictionary (i.e has been created).
        - If not create it with the original node.next value and add it to the dictionary.
        - Point the copy version of the node (dict[node]) next pointer to this newly created node.
    - Check to see if the node.random point to another node. If yes:
        - Check to see if that node already exists in the dictionary (i.e has been created).
        - If not create it with the original node.random value and add it to the dictionary.
        - Point the copy version of the node (dict[node]) random pointer to this newly created node.
    - Continue that until the end of the linked list and return dict[head] (which is the head of the copied linked list).
    - With this method, we create all 3 nodes (if neccessary) at the current node that we are examining. So later on when we hit the node that we are already created and add to the dictionary, all we need to do is updating its next and random pointers.

### Pseudocode
- If head is None return None.
- Initializing variables:
    - cur = head
    - copy_dict = {}
- Go through the linked list until cur is None:
    - Check to see if copy_dict[cur] exists. If not, create it with cur.val 
    - Check to see if cur.next exists. If yes:
        - check is copy_dict[cur.next] exists. If not, create it and add to the dictionary.
        - Update the pointer of copy_dict[cur].next to copy_dict[cur.next].
    - Check to see if cur.random exists. If yes:
        - check is copy_dict[cur.random] exists. If not, create it and add to the dictionary.
        - Update the pointer of copy_dict[cur].random to copy_dict[cur.random].
- Return copy_dict[head].

### BigO
- Go through the list exactly once, so runtime O(N).
- Created a dictionary to store all the nodes and its copied value, so O(N) space.


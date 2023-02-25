### Question
- [Link to question.](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

### Thoughts
- A trie is like a tree, used to store and retrieve keys in datasets of string.
- Since it is a tree, each of the node will have a special characteristic to it.
- TrieNode structure:
    - Children: all the characters that are stored in that node. This should be a dictionary for constant time retrieval.
    - end: is a boolean, indicate if this character markes the end of the string.
- Trie structure:
    - What a trie need: just like a tree, it needs a root node, which is simply a TrieNode.
    - Insert:
        - Assign a curr pointer to be at root to traverse through the trie.
        - Go through each character in the word.
            - If the character does not exist in the current node children list yet, create a new node and add it in (which that character as a key).
            - Move curr node to that node.
        - At the end, assign the curr node end to True (marking the end of the string).
    - Search: similar to insert:
        - Start curr from root.
        - Go through each character of the string
            - if the character does not exist in the children list, return False (word not found).
            - move curr to the next node if it exists.
        - CHeck to see if the last character (curr pointer) end is marked True. if it is then return True, else False. (like app and apple, if we only insert apple then at the 2nd p, end will be False, and app does not exist in the trie).
    - Startswith: very similar to search, just does not need to check the end == True since we just need to the prefix to be in the trie.

### BigO

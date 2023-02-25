### Question
- [Link to question.](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

### Thoughts
- Build this word dictionary out of a trie. Basically the set up is the same with trie node and addWord. But search will be different:
    - There are at most 2 ".". When a "." appears, it means a wild card, and we move on to check the next letter to see if it's in one of the words that are already in the dictionary.
    - The thing is after the ".", where is the next node that we move to? In order to determine that, we have to search all the nodes available in the list of children, hope for 1 of them to match the word.
    - Example: inserted word "dad", "mad", "pad", check to see if there's ".ad"
        - When we see ".", first of all we starts of with the list of children at the root, which is [d,m,p]
        - Choose d, assuming that's what the . means
        - Move on to the next character, which is a. Seach in the children of d to see if a presents. Yes, move on to d.
        - Next character is d. Search in the children of a to see d is there. Yes.
        - d is also the end of the word, so return True.
    - Example: inserted word "dad", "mad", "med", "pad", check to see if there's "m.p"
        - Start with the root. First character is m. we see m in the list of children of root ([d,m,p]), so move on to next character.
        - We see ".". Check all the children of m (in this case only [a,e], but it can be much more in real life). Pretend to go with a.
        - Next character is p. p is not in the list of children of a ([d]), then return False.
        - Come back to the children of m, which is e. Pretend to go with e.
        - next character is p is not in the list of the children of e ([d]). Return False. 
        - No more children of m, then we did not find a match. Return False.
- In order to be able to do this, we need recursion, i.e dfs.
- If the character is not a ".", move on to the next node like normal searching in trie.
- if it is ".", try to search for all the next characters in the list of children of root.
    - dfs(i+1, child), with i being the index of the current root node, child being one of the children of the root node.
    
### BigO

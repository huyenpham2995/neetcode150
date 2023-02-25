class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if curr.children.get(char) is None:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            curr = root

            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if curr.children.get(word[i]) is None:
                        return False
                curr = curr.children[word[i]]

            return curr.end
        return dfs(0, self.root)    
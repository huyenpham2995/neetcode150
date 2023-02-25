class TrieNode:
    def __init__(self):
        self.children = {}
        self.end =  False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if cur.children.get(char) is None:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if cur.children.get(char) is None:
                return False
            cur = cur.children[char]
        
        if cur.end != True:
            return False
        
        return True
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if cur.children.get(char) is None:
                return False
            cur = cur.children[char]
        
        return True
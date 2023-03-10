from typing import List

def partition(s: str) -> List[List[str]]:
    res = []
    p = []

    def backtrack(i):
        if i >= len(s):
            res.append(p.copy())
            return
        
        for j in range(i,len(s)):
            if is_palindrome(s,i,j):
                p.append(s[i:j+1])
                backtrack(j+1)
                p.pop()

    def is_palindrome(word, s, e):
        while s < e:
            if word[s] != word[e]:
                return False
            s += 1
            e -= 1
        
        return True

    backtrack(0)
    return res
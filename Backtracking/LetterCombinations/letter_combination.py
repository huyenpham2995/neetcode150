from typing import List

def letterCombinations(digits: str) -> List[str]:
    num_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    combo = ""

    def dfs(i):
        nonlocal combo
        if len(combo) == len(digits):
            if combo != "":
                res.append(combo)
            return

        for char in num_to_letters[digits[i]]:
            combo += char
            dfs(i+1) 
            combo = combo[:-1]

    dfs(0)
    return res     
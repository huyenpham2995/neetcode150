from collections import defaultdict

def longest_non_repeating_substring(s: str) -> int:
    if len(s) < 2: return len(s)

    l,r = 0, 1
    max_count = 0
    d = defaultdict(int)
    d[s[l]] = 1

    while l<=r<len(s):
        if d[s[r]] != 0:
            max_count = max(r-l, max_count)
            while s[l] != s[r]:
                d[s[l]] = 0
                l += 1
            if l < r:
                l += 1
        else:
            d[s[r]] = 1
        r += 1
    
    return max(r-l, max_count)
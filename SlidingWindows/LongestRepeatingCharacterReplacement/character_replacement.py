from collections import defaultdict

def character_replacement(s: str, k: int) -> int:
    if len(s) < 2: return len(s)

    count = defaultdict(int)
    l=0
    max_char_len = 0
    max_length = 0

    for i in range(len(s)):
        count[s[i]] += 1
        max_char_len = max(max_char_len, count[s[i]])

        if (i-l+1-max_char_len) > k:
            count[s[l]] -= 1
            l += 1
        
        max_length = max(max_length, i-l+1)

    return max_length
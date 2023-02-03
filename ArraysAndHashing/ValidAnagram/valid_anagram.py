def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if s=="" and t=="": return True

    s = sorted(s)
    t = sorted(t) 

    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True
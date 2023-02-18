from collections import defaultdict

def check_inclusion1(s1: str, s2: str) -> bool:
    permutation = [char for char in s1]

    l,r=0,0
    while r<len(s2):
        if s2[r] in permutation:
            permutation.remove(s2[r])
            if len(permutation) == 0:
                return True
            r += 1
        else:
            if len(permutation) == len(s1):
                l += 1
                r += 1
            else:
                permutation.append(s2[l])
                l += 1

    return False

def check_inclusion2(s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False

    count_s1 = defaultdict(int)
    count_s2 = defaultdict(int)

    for i in range(len(s1)):
        count_s1[s1[i]] += 1
        count_s2[s2[i]] += 1

    for i in range(len(s1), len(s2)):
        match = 0
        for char,count in count_s1.items():
            if count_s2[char] == count:
                match += 1
        if match == len(count_s1):
            return True
        count_s2[s2[i-len(s1)]] -= 1
        count_s2[s2[i]] += 1

    match = 0
    for char,count in count_s1.items():
        if count_s2[char] == count:
            match += 1
    if match == len(count_s1):
        return True

    return False

def check_inclusion3(s1: str, s2: str) -> bool:
    pass
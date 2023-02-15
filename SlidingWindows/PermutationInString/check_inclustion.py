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
    pass

def check_inclusion3(s1: str, s2: str) -> bool:
    pass
from typing import List
from math import ceil

def min_eating_speed(piles: List[int], h: int) -> int:
    if len(piles) == h: return max(piles)

    left = 1
    right = max(piles)
    res = max(piles)

    while left <= right:
        speed = (right+left)//2
        time = 0

        for bananas in piles:
            time += ceil(bananas/speed)
        
        if time <= h:
            res = min(speed, res)
            right = speed - 1
        else:
            left = speed + 1
    
    return res
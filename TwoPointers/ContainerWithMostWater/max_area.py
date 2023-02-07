from typing import List

def max_area(height: List[int]) -> int:
    if len(height) < 2: return 0

    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        current_area = (r - l) * min(height[l], height[r])
        if max_area < current_area:
            max_area = current_area
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_area
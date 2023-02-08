from typing import List

def trap(height: List[int]) -> int:
    if len(height) < 2: return 0

    l, r = 0, len(height)-1
    max_left, max_right = height[l], height[r]
    water_trap = 0

    while l <= r:
        trap = 0
        if max_left <= max_right:
            trap = min(max_left, max_right) - height[l]
            if height[l] > max_left:
                max_left = height[l]
            l += 1
        else: 
            trap = min(max_left, max_right) - height[r]
            if height[r] > max_right:
                max_right = height[r]
            r -= 1
        if trap > 0:
            water_trap += trap
    
    return water_trap
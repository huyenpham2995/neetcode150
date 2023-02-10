from typing import List

def largest_rectangle(heights: List[int]) -> int:
    max_rectangle = 0
    heights.append(0)
    stack = [] # (height, index)

    for i in range(len(heights)):
        taken_index = i
        while stack and heights[i] < stack[-1][0]:
            height, taken_index = stack.pop()
            area = height*(i-taken_index)
            if area > max_rectangle:
                max_rectangle = area
        stack.append((heights[i], taken_index))
    
    return max_rectangle
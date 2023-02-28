from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    min_heap = []
    res = []

    for x,y in points:
        distance = x*x + y*y
        heapq.heappush(min_heap, [distance, x, y])
    
    while len(res) < k and min_heap:
        _, x, y = heapq.heappop(min_heap)
        res.append([x,y])
    return res
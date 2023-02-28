import heapq
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    if len(stones) < 2:
        return stones[0]

    max_heap = [w*-1 for w in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        y = heapq.heappop(max_heap)
        x = heapq.heappop(max_heap)

        if y != x: 
            heapq.heappush(max_heap, y-x)
    
    return abs(max_heap[0]) if len(max_heap) > 0 else 0
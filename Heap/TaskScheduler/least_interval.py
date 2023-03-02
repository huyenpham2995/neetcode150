from typing import List
from collections import defaultdict
import heapq

def leastInterval(tasks: List[str], n: int) -> int:
    if n == 0 or len(tasks) < 2:
        return len(tasks)

    task_count = defaultdict(int)

    for task in tasks:
        task_count[task] += 1
    
    max_heap = [[count*-1, task] for task, count in task_count.items()]
    heapq.heapify(max_heap)
    
    time = 0
    while max_heap:
        arr = []
        i = 0

        while i<=n and max_heap:
            count, task = heapq.heappop(max_heap)
            time += 1
            count += 1
            if count < 0: 
                arr.append([count,task])
            i += 1           
        
        for item in arr:
            heapq.heappush(max_heap, item)
        
        if i <= n and max_heap:
            time += n-i+1 

    return time
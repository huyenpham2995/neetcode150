from typing import List
from collections import defaultdict

def top_k_frequent_with_sort(nums: List[int], k: int) -> List[int]:
    if len(nums) < 1: return []
    count_dict = defaultdict(int)

    for num in nums:
        count_dict[num] += 1
    
    sorted_count = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    
    return [x[0] for x in sorted_count[:k]]

def top_k_frequent_with_bucket_list(nums: List[int], k: int) -> List[int]:
    if len(nums) < 1: return []
    count_dict = defaultdict(int)

    for num in nums:
        count_dict[num] += 1

    bucket_sort_nums = [[] for i in range(len(nums)+1)]
    for num, count in count_dict.items():
        bucket_sort_nums[count].append(num)

    result = []
    for items in bucket_sort_nums[-1::-1]:
        result += items
        if len(result) == k:
            return result
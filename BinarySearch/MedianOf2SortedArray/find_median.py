from typing import List

def find_median(nums1: List[int], nums2: List[int]) -> float:
    total_length = len(nums1) + len(nums2)
    half = total_length//2
    
    A, B = nums1, nums2
    if len(nums1) > len(nums2): 
        A, B = nums2, nums1

    l, r = 0, len(A)-1
    median = float("inf")

    while median == float("inf"):
        mid = (l+r)//2

        # index of he last element of the first partition of array B
        i = half-2-mid
        
        A_mid = A[mid] if mid >= 0 else float("-inf")
        A_right = A[mid+1] if mid+1 < len(A)  else float("inf")
        B_mid = B[i] if i >= 0 else float("-inf")
        B_right = B[i+1] if i+1 <len(B) else float("inf")

        # right partition
        if A_mid <= B_right and B_mid <= A_right:
            if total_length % 2 == 0:
                median = (max(A_mid, B_mid) + min(A_right, B_right))/2
            else:
                median = min(A_right, B_right)
        elif A_mid > B_right:
            r = mid - 1
        else:
            l = mid + 1

    return median
from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0: return False

    # find the correct row
    start_r = 0
    end_r = len(matrix) - 1
    row = -1

    while start_r <= end_r and row == -1:
        mid_r = (start_r + end_r)//2
        if matrix[mid_r][0] == target:
            return True
        elif matrix[mid_r][0] < target:
            if matrix[mid_r][-1] >= target:
                row = mid_r
            else: start_r = mid_r + 1
        else:
            end_r = mid_r - 1


    # find the target in the row
    start_c = 0
    end_c = len(matrix[row])-1

    while start_c <= end_c:
        mid_c = (start_c + end_c)//2
        if matrix[row][mid_c] == target:
            return True
        elif matrix[row][mid_c] < target:
            start_c = mid_c + 1
        else:
            end_c = mid_c - 1

    return False
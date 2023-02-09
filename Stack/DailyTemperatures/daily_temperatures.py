from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack!=[] and temperatures[i] > stack[-1][1]:
            index, temp = stack.pop()
            result[index] = i - index
        stack.append([i, temperatures[i]])

    return result
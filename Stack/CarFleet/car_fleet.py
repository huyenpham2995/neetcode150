from typing import List

def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    car_list = [(p,s) for p,s in zip(position, speed)]
    car_list.sort(reverse=True)
    t_stack = []

    for p,s in car_list:
        t_to_target = (target-p)/s
        if t_stack == [] or t_to_target > t_stack[-1]:
            t_stack.append(t_to_target)
    
    return len(t_stack)
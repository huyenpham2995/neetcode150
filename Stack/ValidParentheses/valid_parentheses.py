def is_valid(s: str) -> bool:
    if len(s) % 2 != 0: return False

    check_list = []

    for char in s:
        if char == ")" or char == "}" or char == "]":
            if len(check_list) == 0: return False
            last_char = check_list.pop()
            if char == ")" and last_char != "(": return False
            elif char == "}" and last_char != "{": return False
            elif char == "]" and last_char != "[": return False
        else:
            check_list.append(char)
    
    if len(check_list) != 0: return False
    return True
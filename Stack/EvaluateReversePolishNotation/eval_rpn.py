from typing import List

def eval_RPN(tokens: List[str]) -> int:
    if len(tokens) < 1: return 0

    number_stack = []

    for token in tokens:
        if len(token) > 1 and token.startswith("-") and token[1:].isdigit():
            number_stack.append(0-int(token[1:]))
        elif token.isdigit():
            token = int(token)
            number_stack.append(token)
        else:
            num2 = number_stack.pop()
            num1 = number_stack.pop()
            if token == "+":
                number_stack.append(num1 + num2)
            elif token == "-":
                number_stack.append(num1 - num2)
            elif token == "/":
                number_stack.append(int(num1 / num2))
            else:
                number_stack.append(num1 * num2)

    return number_stack[0]
    
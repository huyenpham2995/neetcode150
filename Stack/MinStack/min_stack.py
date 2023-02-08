class MinStack:
    def __init__(self):
        self.stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self._min_stack == []:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(val, self._min_stack[-1]))

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self._min_stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

        return None

    def getMin(self) -> int:
        return self._min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.stack and not self.minStack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            minimum_value = min(self.minStack[-1], val)
            self.minStack.append(minimum_value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

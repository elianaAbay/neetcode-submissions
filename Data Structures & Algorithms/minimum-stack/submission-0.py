class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        print(self.stack)
        minimum = float("inf")
        for item in self.stack:
            minimum = min(minimum, item)
        return minimum


        
        

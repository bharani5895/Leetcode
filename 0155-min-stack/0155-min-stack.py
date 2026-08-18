class MinStack:

    def __init__(self):
        self.st = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        # Push to minstack if it's empty or val is <= current minimum
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        # If the element being removed is the current minimum, pop from minstack too
        if self.st[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
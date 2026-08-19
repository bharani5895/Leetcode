class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.st:
            self.min_val = val
            self.st.append(val)
        else:
            if val < self.min_val:
                # Push encoded value 2*val - min_val
                self.st.append(2 * val - self.min_val)
                self.min_val = val
            else:
                self.st.append(val)

    def pop(self) -> None:
        top_val = self.st.pop()
        
        # If popped value is less than current min_val, it was an encoded minimum
        if top_val < self.min_val:
            # Restore previous minimum: 2*min_val - top_val
            self.min_val = 2 * self.min_val - top_val

    def top(self) -> int:
        top_val = self.st[-1]
        
        # If top is encoded, actual value is min_val
        if top_val < self.min_val:
            return self.min_val
        return top_val

    def getMin(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
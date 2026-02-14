# Here the idea is to use dual data storage, where every element in the stack
# will be an array of elements: the value of the element and the min element of the stack
# Giving constant time for retrieveing the min element of the stack.
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val

        self.stack.append([val, min_val])
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0] 
        return None
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1] 
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
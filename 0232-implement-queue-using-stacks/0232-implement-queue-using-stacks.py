class MyQueue:
    def __init__(self):
        self.stack_in = []   # for push
        self.stack_out = []  # for pop/peek

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.move_in_to_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.move_in_to_out()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def move_in_to_out(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())





# class MyQueue:

#     def __init__(self):
#         self.stack = []
#         self.temp = []
#         self.count = 0
        

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.count += 1
        

#     def pop(self) -> int:
#         while self.stack:
#             element = self.stack.pop()
#             self.temp.append(element)

#         ele = self.temp.pop()

#         while self.temp:
#             element = self.temp.pop()
#             self.stack.append(element)

#         self.count -= 1
#         return ele

#     def peek(self) -> int:
#         while self.stack:
#             element = self.stack.pop()
#             self.temp.append(element)

#         ele = self.temp.pop()
#         self.temp.append(ele)

#         while self.temp:
#             element = self.temp.pop()
#             self.stack.append(element)

#         return ele
        

#     def empty(self) -> bool:
#         if self.count > 0:
#             return False
#         return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
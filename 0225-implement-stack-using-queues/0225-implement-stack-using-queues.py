from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate all previous elements behind the new one
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()  # always the "top"

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

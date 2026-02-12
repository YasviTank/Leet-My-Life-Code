class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(digits):
            result = []
            for i in range(4):
                digit = str((int(digits[i]) + 1) % 10)
                result.append(digits[:i] + digit + digits[i+1:])
                digit = str((int(digits[i]) - 1 + 10) % 10)
                result.append(digits[:i] + digit + digits[i+1:])
            return result

        q = deque()
        q.append(["0000", 0]) #the digits on the lock, the steps/turns
        visit = set(deadends)

        while q:
            digits, steps = q.popleft()
            if digits == target:
                return steps
        
            for child in children(digits):
                if child not in visit:
                    visit.add(child)
                    q.append([child, steps+1])
        return -1

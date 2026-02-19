class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = []
        result = ""

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                number = int(k)

                substr = number * substr
                stack.append(substr)


        while stack:
            temp.append(stack.pop())
        while temp:
            result+=temp.pop()

        return result
        # or can do : return "".join(stack)

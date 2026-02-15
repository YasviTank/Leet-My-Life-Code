class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])

        stack = []
        operators = ["+", "/", "*", "-"]

        for ele in tokens:
            if ele not in operators:
                stack.append(ele)
            else:
                number1 = int(stack.pop())
                number2 = int(stack.pop())
                if ele == "+":
                    stack.append(number2 + number1)
                elif ele == "-":
                    stack.append(number2 - number1)
                elif ele == "*":
                    stack.append(number2 * number1)
                else:
                    stack.append(int(number2 / number1))


        return stack.pop()
        
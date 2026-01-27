class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack



# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []

#         for element in s:
#             if element == "(" or element == "[" or element == "{":
#                 stack.append(element)
#                 print("appeneded")
#             else:
#                 if len(stack) != 0:
#                     bracket = stack.pop()
#                     print(bracket)
#                     if element == ")" and bracket != "(":
#                         print("1")
#                         return False
#                     elif element == "}" and bracket != "{":
#                         return False
#                     elif element == "]" and bracket != "[":
#                         return False

#                 else:
#                     return False
       
#         if len(stack) != 0:
#             print("end false")
#             return False
#         else:
#             return True

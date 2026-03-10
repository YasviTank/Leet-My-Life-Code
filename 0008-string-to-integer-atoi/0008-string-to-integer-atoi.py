class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1
        
        # 2. Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Check overflow BEFORE adding digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
        
        
        
        
        # int_min = -2**31
        # int_max = 2**31 - 1
        # sign = 1
        # result = ""
        # saw_digit = False
        # saw_sign = False
        # started = False

        # for element in s:
        #     if element == " " and not started:
        #         continue

        #     started = True
        #     if element >= "0" and element <= "9":
        #         result += element
        #         saw_digit = True
        #     elif element == "-":
        #         if saw_digit == False and saw_sign == False:
        #             sign = -1
        #             saw_sign = True
        #         else:
        #             break
        #     elif element == "+":
        #         if saw_digit == False and saw_sign == False:
        #             sign = 1
        #             saw_sign = True
        #         else:
        #             break

        #     else:
        #         break

        
        # if result:
        #     result = sign * int(result)
        #     if result < int_min:
        #         return int_min
        #     elif result > int_max:
        #         return int_max
        #     else:
        #         return result

            
        # else:
        #     return 0
            
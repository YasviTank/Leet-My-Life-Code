class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_min = -2**31
        int_max = 2**31 - 1
        sign = 1
        result = ""
        saw_digit = False
        saw_sign = False
        started = False

        for element in s:
            if element == " " and not started:
                continue

            started = True
            if element >= "0" and element <= "9":
                result += element
                saw_digit = True
            elif element == "-":
                if saw_digit == False and saw_sign == False:
                    sign = -1
                    saw_sign = True
                else:
                    break
            elif element == "+":
                if saw_digit == False and saw_sign == False:
                    sign = 1
                    saw_sign = True
                else:
                    break

            else:
                break

        
        if result:
            result = sign * int(result)
            if result < int_min:
                return int_min
            elif result > int_max:
                return int_max
            else:
                return result

            
        else:
            return 0
            
class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        unit = 1
        s = ""

        while num:
            digit = (num % 10)
            num = num // 10
            if digit == 4 or digit == 9:
                s1 = ""
                if digit == 4:
                    s1 += hashmap[5*unit]
                else: 
                    s1 += hashmap[10*unit]
                s1 += hashmap[1*unit]
                s += s1
            else:
                s1 = ""
                if digit <= 3:
                    for i in range(digit):
                        s1 += hashmap[1 * unit]
                else:
                    digit = digit - 5
                    
                    for i in range(digit):
                        s1 += hashmap[1 * unit]
                    s1 += hashmap[5*unit]
                s += s1
            unit *= 10


        return s[::-1]


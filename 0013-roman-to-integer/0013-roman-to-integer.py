class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = hashmap[s[-1]]

        for letter in s[::-1]:
            num = hashmap[letter]

            if num >= prev:
                result += num
            else:
                result -= num

            prev = num


        return result




    ##XLIX => 10-50= 40, 1-9 = 10
    # 10 -1= 9, 59-10= 49
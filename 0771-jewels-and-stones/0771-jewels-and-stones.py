class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        check = {}
        count  = 0

        for stone in stones:
            if stone in check:
                check[stone] += 1
            else:
                check[stone] = 1

        for jewel in jewels:
            if jewel in check:
                count += check[jewel]

        return count
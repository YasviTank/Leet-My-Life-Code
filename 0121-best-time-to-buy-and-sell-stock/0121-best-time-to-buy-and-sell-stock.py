class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # min_val = float('inf')
        # profit = 0

        # for price in prices:
        #     if min_val > price:
        #         min_val = price
        #     else:

        #         val = price - min_val
        #         if val > profit:
        #             profit = val

        # return profit


        # two pointer method:
        l, r = 0, 1 # l = buy, r = sell
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit

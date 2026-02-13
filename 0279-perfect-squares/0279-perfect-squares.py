class Solution:
    def numSquares(self, n: int) -> int:
        
        # making the array that stores the squares till n
        squares = []
        number = 1
        while (number*number)<=n:
            squares.append(number*number)
            number+=1


        dp = [float("inf")]*(n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for sq in squares:
                if sq > i:
                    break

                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]





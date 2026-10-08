class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        arr = [True] * n
        arr[0] = arr[1] = False

        i = 2
        while i * i < n:
            if arr[i]:
                for num in range(i * i, n, i):
                    arr[num] = False
            i += 1

        return sum(arr)
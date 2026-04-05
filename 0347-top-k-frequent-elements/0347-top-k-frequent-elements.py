class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Here we are doing 1 + what the count of n already is, and if n doesnt exists then we get 0

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
        
        
        
        
        # count = {}

        # for num in nums:
        #     if num not in count:
        #         count[num] = 1
        #     else:
        #         count[num] += 1

        # sorted_nums = sorted(count, key=count.get, reverse=True)
        # return sorted_nums[:k]
            
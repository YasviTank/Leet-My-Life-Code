class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                difference = abs(i - hashmap[nums[i]])
                # print(i, hashmap[nums[i]])
                # print(difference)
                if difference <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
            else:
                hashmap[nums[i]] = i
        return False
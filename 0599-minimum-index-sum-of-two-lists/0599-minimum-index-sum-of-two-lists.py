class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n = len(list1)
        m = len(list2)
        
        hashmap = {}
        result = []
        minimum = n + m

        for i in range(n):
            hashmap[list1[i]] = i

        for i in range(m):
            if list2[i] in hashmap:
                min_sum = i + hashmap[list2[i]]

                if min_sum < minimum:
                    minimum = min_sum
                    result = [list2[i]]
                elif min_sum == minimum:
                    result.append(list2[i])

        return result
        

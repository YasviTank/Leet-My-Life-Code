class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        hashmap = {}
        hashset = set()

        for i in range(n):
            if s[i] not in hashmap:
                if t[i] not in hashset:
                    hashset.add(t[i])
                    hashmap[s[i]] = t[i]
                else:
                    return False
            else:
                
                if hashmap[s[i]] != t[i]:
                    return False
        return True


        

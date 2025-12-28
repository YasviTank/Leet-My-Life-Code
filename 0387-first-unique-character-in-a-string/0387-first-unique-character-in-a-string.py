class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for ch in s:
            if ch in hashmap:
                hashmap[ch] = -1 #repeating character
            else:
                hashmap[ch] = 1
        
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        
        return -1
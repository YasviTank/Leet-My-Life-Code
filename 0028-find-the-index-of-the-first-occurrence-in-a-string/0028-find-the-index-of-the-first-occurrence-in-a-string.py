class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    
        n = len(needle) 
        h = len(haystack) - n
        
        if n > (h+n):
            return -1
        
        for i in range(h + 1):
            if haystack[i:n+i] == needle:
                return i
        return -1
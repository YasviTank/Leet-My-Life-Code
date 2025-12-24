class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        res = ""
        
        for word in words:
            word = word[-1::-1]
            res += word
            res += " "
        return res.strip()
        
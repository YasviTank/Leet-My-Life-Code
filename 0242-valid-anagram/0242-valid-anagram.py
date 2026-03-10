class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hashcount = {}
        
        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in hashcount:
                hashcount[letter] = 1
            else:
                hashcount[letter] += 1

        for letter in t:
            if letter in hashcount:
                if hashcount[letter] > 0:
                    hashcount[letter] -= 1
                else:
                    return False
            else:
                return False
                

        return True


            
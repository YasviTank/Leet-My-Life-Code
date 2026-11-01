class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1


        sorted_s = ""

        for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
            # print(key, value)
            sorted_s += ((key)*value)

        return sorted_s
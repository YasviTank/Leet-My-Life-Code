class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            # create sorted key
            key = "".join(sorted(word))

            if key not in hashmap:
                hashmap[key] = [word]
            else:
                hashmap[key].append(word)

        return list(hashmap.values())

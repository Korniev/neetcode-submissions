class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_map1, hash_map2 = {}, {}
        
        for n in range(len(s)):
            hash_map1[s[n]] = 1 + hash_map1.get(s[n], 0)
            hash_map2[t[n]] = 1 +  hash_map2.get(t[n], 0)

        for i in hash_map1:
            if hash_map1[i] != hash_map2.get(i, 0):
                return False
        return True

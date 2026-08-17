class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash_1, hash_2 = {}, {}

        for i in range(len(s)):
            hash_1[s[i]] = hash_1.get(s[i], 0) + 1
            hash_2[t[i]] = hash_2.get(t[i], 0) + 1
        
        for n in hash_1:
            if hash_1[n] != hash_2.get(n, 0):
                return False
        return True

        

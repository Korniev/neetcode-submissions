class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hash1, hash2 = {}, {}

        for i in range(len(s)):
            hash1[s[i]] = hash1.get(s[i], 0) + 1
            hash2[t[i]] = hash2.get(t[i], 0) + 1

        for n in hash1:
            if hash1[n] != hash2.get(n, 0):
                return False
        return True

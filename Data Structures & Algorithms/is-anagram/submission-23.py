class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash1, hash2 = {}, {}

        for n in range(len(s)):
            hash1[s[n]] = hash1.get(s[n], 0) + 1
            hash2[t[n]] = hash2.get(t[n], 0) + 1
        
        for i in hash1:
            if hash1[i] != hash2.get(i, 0):
                return False        
        return True
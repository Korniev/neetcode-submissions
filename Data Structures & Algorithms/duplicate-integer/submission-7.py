class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_result = set()

        for n in nums:
            if n in hash_result:
                return True
            hash_result.add(n)
        return False
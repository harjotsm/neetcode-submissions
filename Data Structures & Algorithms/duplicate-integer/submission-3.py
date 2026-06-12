class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateFree = set(nums)

        if len(nums) != len(duplicateFree):
            return True
        return False
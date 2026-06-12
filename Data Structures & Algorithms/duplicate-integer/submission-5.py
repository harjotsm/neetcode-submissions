class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = set()

        for i in nums:
            if i in nums_map:
                return True
            nums_map.add(i)
        return False
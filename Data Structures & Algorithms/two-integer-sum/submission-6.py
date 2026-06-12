class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addend_map = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in addend_map:
                return [addend_map[diff],i]
            addend_map[n] = i

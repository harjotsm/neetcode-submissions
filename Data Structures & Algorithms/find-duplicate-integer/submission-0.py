class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker = set()

        for i in range(len(nums)):
            if nums[i] in tracker: 
                return nums[i]
            
            else:
                tracker.add(nums[i])
                i += 1

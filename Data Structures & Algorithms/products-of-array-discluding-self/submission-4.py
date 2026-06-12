class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix & suffix
        '''
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
        '''

        # optimal in O(n)
        n = len(nums)
        res = [1] * n
        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



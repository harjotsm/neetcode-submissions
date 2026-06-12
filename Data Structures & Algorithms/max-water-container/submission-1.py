class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        # area = l * h -> diff between both pointers * hieght of lower bar 

        while l < r: 
            diff = r - l
            area = diff * min(heights[l], heights[r]) 
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

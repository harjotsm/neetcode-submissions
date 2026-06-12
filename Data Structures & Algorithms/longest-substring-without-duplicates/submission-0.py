class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        lib = {}
        res = 0

        for r in range(len(s)):
            if s[r] in lib:
                l = max(lib[s[r]] + 1, l)
            lib[s[r]] = r
            res = max(res, r - l + 1)
        return res



            

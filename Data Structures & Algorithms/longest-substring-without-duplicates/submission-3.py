class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charMap = {}
        maxSub = 0

        for r in range(len(s)):
            if s[r] in charMap:
                l = max(charMap[s[r]] + 1,l)
            charMap[s[r]] = r
            maxSub = max(maxSub, r-l+1)
        return maxSub
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxRep = 0
        count_mp = {}
        res = 0

        for r in range(len(s)):
            # updating the counter in map
            count_mp[s[r]] = 1 + count_mp.get(s[r], 0)
            maxRep = max(count_mp[s[r]], maxRep)

            # case: we hit k & shrink window
            while (r-l + 1) - maxRep > k:
                count_mp[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res


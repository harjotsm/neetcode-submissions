class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m*n*26) <= O(m*n), where m = number of input strs & n = avg. len of one strs

        # use defaultdict because with normal dict we get KeyError, because we try to append(s) to res although there is no key for res
        res = defaultdict(list)

        # we use character freq
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # use tuple because it ist inmutable, lists are mutable => python forbids using mutable keys/indexes
            res[tuple(count)].append(s)

        # need to reuturn a list
        return list(res.values())

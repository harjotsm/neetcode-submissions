class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m*n*26) <= O(m*n), where m = number of input strs & n = avg. len of one strs
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

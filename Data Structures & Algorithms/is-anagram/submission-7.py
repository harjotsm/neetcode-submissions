class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cleanS = Counter(s)
        cleanT = Counter(t)

        if cleanS != cleanT:
            return False
        return True


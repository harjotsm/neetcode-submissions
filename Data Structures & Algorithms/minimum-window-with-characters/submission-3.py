class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # countT keeps track of elements in t with Hashmap
        # window keeps track of our current chars in Hashmap 
        countT, window = {}, {}
        # fill the Hashmap with t values
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # we use integer values to compare if the requirement is met -> faster thank comparing 
        have, need = 0, len(countT)

        res, resLen = [-1, -1], float("infinity")
        l = 0 
        # iter over s with pointer 
        for r in range(len(s)):
            c = s[r]
            # fill the window Hashmap
            window[c] = 1 + window.get(c, 0)

            # check if current char is in our window & if reached the needed number of matching chars?
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # if we founf a matching window we check if it is smaller than the previous 
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # delete the most left element from window
                window[s[l]] -= 1
                # ensure that the deleted elemnt was not needed
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1 # if so schrink the window 
        # get the best coordinates & return output
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
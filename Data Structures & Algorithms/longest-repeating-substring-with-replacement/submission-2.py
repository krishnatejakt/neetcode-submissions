class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        res = 0

        maxF = 0

        for r in range(0, len(s)):
            if s[r] not in d:
                d[s[r]] = 0
            
            d[s[r]]+=1

            maxF = max(maxF, d[s[r]])

            while (r - l + 1) - maxF > k:
                d[s[l]]-=1
                l+=1
            
            res = max(res, r - l + 1)
        return res
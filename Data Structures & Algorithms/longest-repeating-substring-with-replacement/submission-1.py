class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        res = 0

        for r in range(0, len(s)):
            if s[r] not in d:
                d[s[r]] = 0
            
            d[s[r]]+=1

            while (r - l + 1) - max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            
            res = max(res, r - l + 1)
        return res
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        l,r = 0, 0

        d = {}

        for char in s1:
            if char not in d:
                d[char] = 0
            d[char]+=1

        while r < len(s2):

            if s2[r] in d:
                start = r
                length = 0

                while r < len(s2) and s2[r] in d and length < len(s1) and d[s2[r]]!=0:
                    d[s2[r]]-=1
                    length+=1
                    r+=1
                if length == len(s1):
                    return True
                else:
                    l = start
                    while l < r:
                        d[s2[l]]+=1
                        l+=1
                    r = start
            r+=1
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        d_s = {}
        d_t = {}

        for char1 in s:
            if char1 not in d_s:
                d_s[char1] = 0
            d_s[char1]+=1
        
        for char2 in t:
            if char2 not in d_t:
                d_t[char2] = 0
            d_t[char2]+=1
        
        for key in d_s:
            if key not in d_t:
                return False
            else:
                if d_s[key]!=d_t[key]:
                    return False
        return True
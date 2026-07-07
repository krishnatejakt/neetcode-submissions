class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        result = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = []
            d[sorted_word].append(word)
        
        for key in d:
            result.append(d[key])
        return result
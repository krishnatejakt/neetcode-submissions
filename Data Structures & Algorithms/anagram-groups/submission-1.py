class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            temp = [0]*26
            for char in word:
                temp[ord(char) - ord('a')]+=1
            temp = tuple(temp)
            if temp not in result:
                result[temp] = []
            result[temp].append(word)
        final_result = []

        for key in result:
            final_result.append(result[key])
        return final_result
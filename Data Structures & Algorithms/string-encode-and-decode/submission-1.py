class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        temp = '€'
        for word in strs:
            for char in word:
                result+=chr(ord(char) + ord('@'))
            result+=temp
        return result

    def decode(self, s: str) -> List[str]:
        words = s.split('€')
        result = []
        for word in words:
            temp = ''
            for char in word:
                temp+=chr(ord(char) - ord('@'))
            result.append(temp)
        return result[0:len(result)-1]
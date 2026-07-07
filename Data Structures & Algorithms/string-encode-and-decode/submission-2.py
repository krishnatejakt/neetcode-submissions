class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding_character = '#'
        encoded_str = ''
        for word in strs:
            encoded_str+=str(len(word)) + encoding_character + word
        return encoded_str


    def decode(self, s: str) -> List[str]:
        result = []
        print(s)
        i = 0
        temp = ''
        while i<len(s):
            if s[i] == '#':
                length = int(temp)
                result.append(s[i+1:i+length+1])
                temp=''
                i+=length+1
            else:
                temp+=s[i]
                i+=1
        return result

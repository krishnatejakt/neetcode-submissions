class Solution:

    def __init__(self):
        self.character = '#'
        self.encoded_string = ''

    def encode(self, strs: List[str]) -> str:
        for string in strs:
            temp = str(len(string)) + self.character
            self.encoded_string+=temp+string
        return self.encoded_string

    def decode(self, s: str) -> List[str]:
        
        temp_number = ''
        result = []

        index = 0
        print(s)

        while index < len(self.encoded_string):
            if self.encoded_string[index]!=self.character:
                temp_number+=self.encoded_string[index]
                index+=1
            else:
                index+=1
                temp_number = int(temp_number)
                result.append(self.encoded_string[index:index+temp_number])
                index+=temp_number
                temp_number = ''
                

        return result


            

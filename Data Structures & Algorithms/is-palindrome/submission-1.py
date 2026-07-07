class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ''

        for character in s:
            if character.isalnum() and s!=" ":
                final_string+=character.lower()
        return final_string == final_string[::-1]
        
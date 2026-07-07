class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parantheses = {')':'(', '}': '{', ']':'['}

        for char in s:
            if not stack and char in open_parantheses:
                return False
            else:
                if char in open_parantheses:
                    if stack[-1] == open_parantheses[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
        return len(stack) == 0
        
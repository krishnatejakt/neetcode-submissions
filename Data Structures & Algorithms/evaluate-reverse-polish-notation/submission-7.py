class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        def check_int(s):
            if s[0] in ('-'):
                return s[1:].isdigit()
            return s.isdigit()

        for token in tokens:
            if check_int(token):
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                else:
                    stack.append(math.trunc(b/a))
        return stack[-1]
                
        
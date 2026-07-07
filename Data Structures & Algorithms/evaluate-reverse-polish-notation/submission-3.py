class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tokens = tokens[::-1]

        if len(tokens) == 1:
            return int(tokens[0])

        while tokens:
            token = tokens.pop()

            if token not in '+-*/':
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
        return stack[-1]
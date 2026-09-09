class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append([i, temperatures[i]])
            else:
                while stack and temperatures[i] > stack[-1][1] :
                    index, temperature = stack.pop()
                    result[index] = i - index

                stack.append([i, temperatures[i]])
        return result
        
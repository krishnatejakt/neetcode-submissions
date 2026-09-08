class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 1:
            return 0
        
        i, j = 0, len(heights) - 1
        result = 0

        while i<j:
            container = min(heights[i], heights[j]) * (j-i)
            result = max(result, container)

            if(heights[i] < heights[j]):
                i+=1
            else:
                j-=1
        return result
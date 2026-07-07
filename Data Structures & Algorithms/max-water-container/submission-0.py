class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return sum(heights)

        max_quantity = 0
        while left < right:
            temp  = (right - left) * min(heights[left], heights[right])

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            max_quantity = max(max_quantity, temp)
        return max_quantity
            
            
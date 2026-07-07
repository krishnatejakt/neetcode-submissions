class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0
        
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        for j in range(len(height)-1, 0, -1):
            maxRight[j-1] = max(maxRight[j], height[j])
        
        result = 0
        for i in range(0, len(height)):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp > 0:
                result+=temp
        return result
        
        
        
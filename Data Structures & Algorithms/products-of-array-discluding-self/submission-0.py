class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(0, len(nums) - 1):
            left[i+1] = left[i] * nums[i]
        
        for j in range(len(nums)-1, 0, -1):
            right[j-1] = right[j] * nums[j]
        
        return [ a * b for a,b in zip(left, right)]
        
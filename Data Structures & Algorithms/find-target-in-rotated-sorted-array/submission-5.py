class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        pivot = l

        if target >= nums[0] and pivot > 0:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1
        
        while left <= right:
            m = (left + right) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return -1
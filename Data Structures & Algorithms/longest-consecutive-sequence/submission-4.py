class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 1

        nums = set(nums)

        if len(nums) == 0:
            return 0

        for num in nums:
            if num+1 in nums:
                continue
            else:
                temp = num
                i = 0
                while temp in nums:
                    temp-=1
                    i+=1
                
                result = max(result, i)
        return result
        
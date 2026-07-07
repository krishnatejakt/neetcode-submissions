class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        if len(nums) == 0:
            return 0
            
        max_consecutive = 1
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                temp = 0
                while num in nums:
                    temp+=1
                    num+=1
            max_consecutive = max(temp, max_consecutive)
        return max_consecutive
        
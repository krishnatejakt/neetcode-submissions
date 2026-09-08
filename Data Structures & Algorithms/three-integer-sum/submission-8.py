class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            
            j,k = i+1, len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    k-=1
        d = {}

        for value in result:
            d[tuple(value)] = 1

        return [list(key) for key in d]
        
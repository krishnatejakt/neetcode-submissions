class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(0, len(nums)):
            new_target = -nums[i]
            if i!=0 and (nums[i-1] == nums[i]):
                continue
            else:
                left, right = i + 1, len(nums) - 1
                while left<right:
                    if nums[left] + nums[right] == new_target:
                        result.append([nums[left], nums[right], nums[i]])
                        left+=1
                        right-=1
                    elif nums[left] + nums[right] > new_target:
                        right-=1
                    else:
                        left+=1
        unique = set()
        for my_list in result:
            unique.add(tuple(my_list))
        return list(unique)
                    
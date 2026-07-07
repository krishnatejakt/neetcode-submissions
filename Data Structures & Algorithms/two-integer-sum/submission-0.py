class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i, element in enumerate(nums):
            if element not in d:
                d[target - element] = i
            else:
                return [d[element], i]
        return -1
        
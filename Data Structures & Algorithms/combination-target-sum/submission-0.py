class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []

        def dfs(i, cur, total):
            if total > target or i >= n:
                return

            if total == target:
                result.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i+1, cur, total)
            
        
        dfs(0,[],0)
        return result
        
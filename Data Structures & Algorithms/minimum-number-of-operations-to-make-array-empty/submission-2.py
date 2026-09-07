class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}

        def dfs(n):
            if n < 0:
                return float("inf")
            if n in [2,3]:
                return 1
            if n in cache:
                return cache[n]
        
            res = min(dfs(n-2), dfs(n-3))
            
            if res == -1:
                return -1
            cache[n] = res + 1
            
            return res + 1
        
        count = Counter(nums)

        res = 0

        for n,c in count.items():
            op = dfs(c)
            if op == float("inf"):
                return -1
            res+=op
            
        return res
        
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        values = []

        for key, value in counter.items():
            values.append([value, key])
        
        if len(nums)<=1:
            return nums
        
        result = []

        heapq.heapify(result)

        for i in range(0, len(values)):
            if len(result) == k:
                if values[i][0] > result[0][0]:
                    heapq.heappop(result)
                    heapq.heappush(result, values[i])
            else:
                heapq.heappush(result, values[i])  
        return [ value for key, value in result]
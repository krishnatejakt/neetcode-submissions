import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = collections.Counter(nums)

        if len(nums) == 0:
            return []

        result = []
        i = 0

        for key, value in num_counter.items():
            result.append([value, key])
        
        final_result = result[0:k]
        heapq.heapify(final_result)

        for value, key in result[k:]:
            if value > final_result[0][0]:
                heapq.heappop(final_result)
                heapq.heappush(final_result, [value, key])
        
        return [key for value, key in final_result]



        




        
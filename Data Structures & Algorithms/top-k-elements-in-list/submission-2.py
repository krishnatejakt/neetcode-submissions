import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num]+=1
        temp_heap = []
        result = []
        for key, value in d.items():
            temp_heap.append([value, key])
        heapq.heapify(result)
        for value in temp_heap:
            if len(result)<k:
                heapq.heappush(result, value)
            else:
                if value[0]>result[0][0]:
                    heapq.heapreplace(result, value)
        return [value[1] for value in result]
        
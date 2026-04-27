import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = defaultdict(int)
        res = []
        count = 0
        for num in nums:
            counts[num] += 1
        for key in counts:
            heapq.heappush(heap, (counts[key], key))
            count += 1
            if count > k:
                heapq.heappop(heap)
                count -= 1
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


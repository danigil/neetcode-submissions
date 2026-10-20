import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heapq.heappop_max(stones)

            if y > stones[0]:
                heapq.heapreplace_max(stones, y-stones[0])
            else:
                heapq.heappop_max(stones)
        
        if len(stones)==0:
            return 0
        else:
            return stones[0]
import heapq
import math
class Solution:
    def dist(self, point: List[int]) -> float:
        x,y=point
        return math.sqrt(x**2 + y**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(self.dist(point), point) for point in points]
        heapq.heapify_max(heap)

        while len(heap) > k:
            heapq.heappop_max(heap)

        return [tup[1] for tup in heap]
        
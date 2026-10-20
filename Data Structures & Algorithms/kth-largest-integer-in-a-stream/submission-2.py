import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l=nums
        # heapq.heapify_max(self.l)
        self.k=k
        

    def add(self, val: int) -> int:
        self.l.append(val)
        self.l.sort()

        return self.l[len(self.l)-self.k]
        # heapq.heappush_max(self.l, val)
        # return self.l[self.k-1]
        

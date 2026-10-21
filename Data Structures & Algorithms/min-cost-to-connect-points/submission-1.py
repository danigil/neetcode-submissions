class Solution:
    def prim(self, edges):
        start=next(iter(edges))
        heap=[(0, start)]
        
        visited=set()
        ret = 0
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
        
            visited.add(curr_node)
            ret+= curr_dist
            
            for (neighbor, neighbor_dist) in edges[curr_node]:
                if not neighbor in visited:
                    heapq.heappush(heap, (neighbor_dist, neighbor))			
        return ret
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        dist = lambda a,b: int(abs(a[0] - b[0]) + abs(a[1] - b[1]))
        edges=defaultdict(set)
        for i, a in enumerate(points):
            for j, b in enumerate(points):
                if i==j:
                    continue
                dist_curr = dist(a,b)
                edges[i].add((j, dist_curr))

        return self.prim(edges)
class Solution:
    def dijkstra(self, edges, n, k):
        heap=[(0,k)]
        heapq.heapify(heap)

        ret = {k: 0}
        done = set()

        while heap:
            val, curr = heapq.heappop(heap)
            if curr in done:
                continue
            
            done.add(curr)
            ret[curr]=val

            for (v,w) in edges[curr]:
                # --- POST-TIMER FIXES ---
                if not v in done:
                    heapq.heappush(heap, (val+w, v))

        return ret
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=defaultdict(set)
        for (u,v,w) in times:
            edges[u].add((v,w))

        d=self.dijkstra(edges, n, k)
        if len(d) < n:
            return -1
        else:
            return max(d.values())
        # m=max(d)
        # # --- POST-TIMER FIXES ---
        # if m == float('inf'):
        #     return -1
        # else:
        #     return m

        
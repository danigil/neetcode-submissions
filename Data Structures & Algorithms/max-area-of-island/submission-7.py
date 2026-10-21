from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visited = set()
        n,m = len(grid), len(grid[0])

        is_land = lambda tup: 0 <= tup[0] < n and 0 <= tup[1] < m and grid[tup[0]][tup[1]]

        def bfs(start):
            q=deque([start])
            curr_area = 0
            while q:
                i,j = q.popleft()
                if not grid[i][j]:
                    continue
                
                grid[i][j] = 0
                curr_area += 1

                l = i, j-1
                r = i, j+1
                u = i-1, j
                d = i+1, j
                neighbors = filter(is_land, [l,r,u,d])
                q.extend(list(neighbors))

            return curr_area
        maxarea = 0
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    continue
                
                area=bfs((i,j))
                maxarea = max(maxarea, area)
        
        return maxarea



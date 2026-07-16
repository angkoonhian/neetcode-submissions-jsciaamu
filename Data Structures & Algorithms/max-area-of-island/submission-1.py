from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        queue = deque([])
        max_area = 0

        def bfs(grid, queue):
            area = 1
            while queue:
                I,J = queue.popleft()
                for i, j in [I+1,J],[I-1,J],[I,J+1],[I,J-1]:
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                        queue.append([i,j])
                        grid[i][j] = "#"
                        area += 1
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append([i,j])
                    grid[i][j] = "#"
                    area = bfs(grid, queue)
                    max_area = max(area, max_area)
        return max_area
                
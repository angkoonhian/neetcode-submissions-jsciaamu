from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        store = defaultdict()
        queue = deque([])
        # We will do it from every single treasure chest independently
        def bfs(grid, queue):
            steps_range = len(queue)
            counter = 1
            while queue:
                if steps_range == 0:
                    steps_range = len(queue)
                    counter += 1
                I,J = queue.popleft()
                for i, j in [I+1,J],[I-1,J],[I,J+1],[I,J-1]:
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > counter:
                        queue.append([i,j])
                        grid[i][j] = counter
                steps_range -= 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i,j])

        bfs(grid, queue)

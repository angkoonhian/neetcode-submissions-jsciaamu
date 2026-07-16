from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque([])

        def bfs(grid, queue, fresh):
            counter_batch = len(queue)
            counter = 0
            while queue:
                if counter_batch == 0:
                    counter_batch = len(queue)
                    counter += 1
                I,J = queue.popleft()
                for i, j in [I+1,J],[I-1,J],[I,J-1],[I,J+1]:
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                        queue.append([i,j])
                        grid[i][j] = "#"
                        fresh -= 1
                counter_batch -= 1
            if fresh != 0:
                return -1
            return counter

        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1

        return bfs(grid, queue, fresh)




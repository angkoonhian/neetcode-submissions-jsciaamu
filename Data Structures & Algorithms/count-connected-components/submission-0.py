from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = { c: [] for c in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        queue = deque([])

        visit, seen = set(), set()
        res = 0
        def dfs(c):
            if c in visit:
                return True
            if c in seen:
                return False
            seen.add(c)
            visit.add(c)
            for neighbor in graph[c]:
                if dfs(neighbor) == False:
                    return False
            seen.remove(c)
            
        print(graph)
        print(visit)
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1

        return res
            
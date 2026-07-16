class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = { c: [] for c in range(numCourses)}
        for p in prerequisites:
            graph[p[0]].append(p[1])

        visit, seen = set(), set()
        res = []
        def dfs(c):
            if c in visit:
                return True
            if c in seen:
                return False
            seen.add(c)
            for neighbors in graph[c]:
                if dfs(neighbors) == False:
                    return False
            seen.remove(c)
            visit.add(c)
            res.append(c)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False

        return len(res) == numCourses

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = { c: [] for c in range(numCourses)}
        for p in prerequisites:
            graph[p[0]].append(p[1])
        res = []
        visit, seen = set(), set()
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
                return []

        return res
            

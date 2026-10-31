class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #detect cycles, if cycle then false
        premap = {}
        for i in range(numCourses):
            premap[i] = []
        
        for course,prereq in prerequisites:
            premap[course].append(prereq)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if premap[crs] == []:
                return True
            
            visiting.add(crs)
            for prereq in premap[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            premap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


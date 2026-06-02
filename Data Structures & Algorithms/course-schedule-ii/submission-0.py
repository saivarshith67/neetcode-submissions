class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}

        visit, cycle = set(), set()

        output = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output

        
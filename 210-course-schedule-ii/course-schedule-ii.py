class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_To_Preq_Map=defaultdict(list)
        cycle=set()
        visited=set()
        res=[]

        for course, preq in prerequisites:
            course_To_Preq_Map[course].append(preq)

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            cycle.add(course)
            for x in course_To_Preq_Map[course]:
                if dfs(x) ==False:
                    return False
                
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if dfs(i)==False: return []
        return res
        
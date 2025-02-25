class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting=set()
        hashmap=defaultdict(list)

        def dfs(course):
            
            if course in visiting: return False

            if hashmap[course]==[]:
                return True
            visiting.add(course)
            
            for preq in hashmap[course]:
                if not dfs(preq):
                    return False
            visiting.remove(course)
            hashmap[course] = []
            return True

        for course,preq in prerequisites:
                hashmap[course].append(preq)

        for course in range(numCourses):
            if not dfs(course): return False
        return True
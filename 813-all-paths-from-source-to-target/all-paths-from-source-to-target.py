class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol=[]
        res=[]
        adj_map=defaultdict(list)
        for i,values in enumerate(graph):
            adj_map[i]=values

        def dfs(node):

            sol.append(node)

            if node==len(adj_map)-1:
                res.append(sol.copy())
                sol.pop()
                return


            for neigh in adj_map[node]:
                dfs(neigh)
            sol.pop()

        dfs(0)
        
        return res

        

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:


        res = []

        def dfs(node, path):
            path.append(node)
            
            # If we reach the last node, store the path
            if node == len(graph) - 1:
                res.append(path.copy())  # Store a copy of the path
            else:
                for neigh in graph[node]:  # Directly use graph[node]
                    dfs(neigh, path)
            
            path.pop()  # Backtrack

        dfs(0, [])  # Start DFS from node 0 with an empty path
        return res
        # sol=[]
        # res=[]
        # adj_map=defaultdict(list)
        # for i,values in enumerate(graph):
        #     adj_map[i]=values

        # def dfs(node):

        #     sol.append(node)

        #     if node==len(adj_map)-1:
        #         res.append(sol.copy())
        #         sol.pop()
        #         return


        #     for neigh in adj_map[node]:
        #         dfs(neigh)
        #     sol.pop()

        # dfs(0)
        
        # return res

        

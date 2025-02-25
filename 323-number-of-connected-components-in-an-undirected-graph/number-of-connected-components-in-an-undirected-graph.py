class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap=defaultdict(list)
        visited=set()
        count=0
        for node1,node2 in edges:
            hashmap[node1].append(node2)
            hashmap[node2].append(node1)
        def dfs(node,prevValue):
            if node in visited:
                return
            visited.add(node)
            for x in hashmap[node]:
                if x==prevValue:
                    continue
                dfs(x,node)
        for i in range(n):
            if i in visited:
                continue
            count+=1
            dfs(i,-1)
        print(visited)
        return count
        
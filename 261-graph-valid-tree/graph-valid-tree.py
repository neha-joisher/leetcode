class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap=defaultdict(list)
        visited=set()

        for node1,node2 in edges:
            hashmap[node1].append(node2)
            hashmap[node2].append(node1)

        def dfs(node,prevValue):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in hashmap[node]:
                if neighbor ==prevValue:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True

        return dfs(0,-1) and len(visited)==n
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap=defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            hashmap[a].append([b,values[i]])
            hashmap[b].append([a,1/values[i]])

        def bfs(src, target):
            if src not in hashmap or target not in hashmap:
                return -1
            
            visited=set()
            q=deque()

            q.append([src,1])
            visited.add(src)

            while q:
                node, weight =q.popleft()
                if node==target:
                    return weight

                for n, w in hashmap[node]:
                    if n not in visited:
                         q.append([n, weight*w])
                         visited.add(n)
            return -1
            
        return [bfs(i[0],i[1]) for i in queries]

        
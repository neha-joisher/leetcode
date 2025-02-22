class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res,sol=[],[]

        def backtrack():
            if len(sol)==n:
                res.append("".join(sol))
                return

            for c in ["a","b","c"]:
                #Restrictions- when sol is empty then you cannot compare sol[-1]- it will throw error
                if not sol or sol[-1] != c:
                        sol.append(c)      # Choose
                        backtrack()        # Explore
                        sol.pop()          # Un-choose (backtrack)
            
        backtrack()
        print(res)
        if len(res)>=k:
            return res[k-1]
        else: return ""

        
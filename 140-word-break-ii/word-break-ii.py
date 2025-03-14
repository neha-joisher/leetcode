class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        def dfs(sol,i):
            if i==len(s):
                res.append(" ".join(sol))
                return
            
            for word in wordDict:
                if i+len(word)<=len(s) and word==s[i:i+len(word)]:
                    sol.append(word)
                    dfs(sol,i+len(word))
                    sol.pop()
        dfs([],0)
        return res
            

        
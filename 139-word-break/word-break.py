class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)

        # def dfs(i):
        #     if i==len(s):
        #         return True
        #     for c in wordDict:
        #         if c==s[i:i+len(c)]:
        #             if dfs(i+len(c)):
        #                 return True
        #     return False
        # return dfs(0)
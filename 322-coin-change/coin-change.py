class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[amount] if dp[amount] != amount + 1 else -1
        
        
        
        
        
        
        
        
        
        # min_coin=float("inf")
        # res=[]
        # sol=[]
        # def dfs(add):
        #     nonlocal min_coin
        #     if len(sol) >= min_coin:
        #         return

        #     if add==amount:
        #         if len(sol)<min_coin:
        #             min_coin=len(sol)
        #             return 
        #     if add>amount:
        #         return
        #     for i in coins:
        #         sol.append(i)
        #         dfs(add+i)
        #         sol.pop()
        # dfs(0)
        # result = min_coin if min_coin != float("inf") else -1
        # return result

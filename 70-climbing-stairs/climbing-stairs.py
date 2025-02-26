class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 1.Recursion
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        # 2.Top Down Approach - Memoization
        # memo={1:1,2:2}
        # def climb(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x]=climb(x-1)+climb(x-2)
        #         return memo[x] 
        # return climb(n)

        # 3. Bottom Up Approach: Using loops
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # dp=[0]*(n+1)
        # dp[1]=1
        # dp[2]=2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]


        # 3. Bottom Up Approach: Memory Optimization
        if n==1:
            return 1
        if n==2:
            return 2
        prev=1
        curr=2
        for i in range(3,n+1):
            prev,curr=curr,prev+curr
        return curr        
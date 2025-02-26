class Solution:
    def fib(self, n: int) -> int:
        
        # 1: Recurssion
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # return self.fib(n-1)+self.fib(n-2)

        # 2. Top Down - Mmemoization
        # memo={0:0, 1:1}
        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x]=f(x-1)+f(x-2)
        #         return memo[x]
        # return f(n)

        if n==0:
            return 0
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]



        
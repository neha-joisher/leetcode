class Solution:
    def fib(self, n: int) -> int:
        
        # 1: Recurssion
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # return self.fib(n-1)+self.fib(n-2)
        # Time Complexity is O(2^n)


        # 2. Top Down - Memoization
        # memo={0:0, 1:1}
        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x]=f(x-1)+f(x-2)
        #         return memo[x]
        # return f(n)
        # Time and Space Complexity is O(n)


        # 3. Bottom Up 
        # you need this base cases because what if the input is 0 or 1, the loop will give index out of bound error
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # print(dp)
        # return dp[n]
        # Time and Space Complexity is O(n)

        # 4. Bottom up - constant memory space complexity O(1)
        if n==0:
            return 0
        if n==1:
            return 1

        prev=0
        curr=1
        for i in range(2,n+1):
            prev,curr=curr,curr+prev
        return curr





        
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def rob_range(start, end):
            dp = [0] * (end - start)
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(2, end - start):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i])
            return dp[-1]

        ans1 = rob_range(0, n - 1)  # Excluding the last house
        ans2 = rob_range(1, n)  # Excluding the first house

        return max(ans1, ans2)
        # n=len(nums)
        # if n==1:
        #     return nums[0]
        # if n==2:
        #     return max(nums[0],nums[1])

        # dp=[0]*(n-1)
        # dp[0]=nums[0]
        # dp[1]=max(nums[1],nums[0])
        # for i in range(2,n-1):
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        # ans1=dp[-1]
        
        # dp=[0]*(n)
        # dp[0]=nums[0]
        # dp[1]=(nums[1])
        # dp[2]=max(nums[1],nums[2])
        # for i in range(3,n):
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        # ans2=dp[-1]
        # return(max(ans1,ans2))
        
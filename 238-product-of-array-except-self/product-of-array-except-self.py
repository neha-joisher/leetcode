class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result=[1]*len(nums)

        prefix=1
        for i in range(1,len(nums)):
            result[i]=nums[i-1] * prefix
            prefix=result[i]
        print(result)

        postfix=1
        for i in range(len(nums)-2,-1,-1):
            postfix*=nums[i+1]
            result[i]*=postfix
        

        return result
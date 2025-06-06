class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                if n+nums[l]+nums[r]>0:
                    r-=1
                elif n+nums[l]+nums[r]<0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    r-=1
        return res
        # res=[]
        # nums.sort()
        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]:
        #             continue 
        #     l=i+1
        #     r=len(nums)-1
        #     while(l<r):
        #         if nums[l]+nums[r]+a>0:
        #             r-=1
        #         elif nums[l]+nums[r]+a<0:
        #             l+=1
        #         else:
        #             res.append([a,nums[l],nums[r]])
        #             l += 1
        #             r -= 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
        # return res
            
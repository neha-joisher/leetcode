class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # num_set=set(nums)
        # l,r=0,len(nums)-1
        # while(l<r):
        #     add=(nums[l]+nums[r])
        #     if -add in num_set:
        #         res.append([nums[l],nums[r],-add])
        #     l+=1
        #     r-=1
        # print(res)
        # return res

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r+ 1] and l < r:
                        r -= 1
                        
        return res
            


        # res=[]
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if (nums[i]+nums[j]+nums[k]==0):
        #                 res.append([nums[i],nums[j],nums[k]])

        # print(res)
        # return res


        
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            print(i)
            if i!=len(nums)-1:
                if nums[i]==nums[i+1]:
                    nums[i]=nums[i]*2
                    nums[i+1]=0
            if nums[i]!=0:
                res.append(nums[i])
        print(res)
        len_res=len(res)
        len_nums=len(nums)
        count=len_nums-len_res
        res.extend([0]*(count))
        print(res)
        return res

        # i=0
        # while(i<len(nums)-1):
        #     if nums[i]==0:
        #         temp=i
        #         while(nums[i]==0):
        #             i+=1
        #         nums[temp]=nums[i]
        #         nums[i]=0
        #         i+=1
        print()



        
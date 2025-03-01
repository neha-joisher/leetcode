class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            # if i!=len(nums)-1:
                if nums[i]==nums[i+1]:
                        nums[i]=nums[i]*2
                        nums[i+1]=0
        temp=0 
        #temp variable will keep track of where the next non zero index is
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[temp]=nums[i]
                temp+=1
        for i in range(temp,len(nums)):
            nums[i]=0
        return nums



        
            


        # res=[]
        # for i in range(len(nums)-1):
        #     if i!=len(nums)-1:
        #         if nums[i]==nums[i+1]:
        #             nums[i]=nums[i]*2
        #             nums[i+1]=0
        #         if nums[i]!=0:
        #             res.append(nums[i])
        # len_res=len(res)
        # len_nums=len(nums)
        # count=len_nums-len_res
        # res.extend([0]*(count))
        # return res



        
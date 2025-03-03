class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        count=0
        smaller=[]
        larger=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                smaller.append(nums[i])
            elif nums[i]>pivot:
                larger.append(nums[i])
            elif nums[i]==pivot:
                count+=1
            
        for i in range(count):
            smaller.append(pivot)
        smaller.extend(larger)
        return smaller
                

        
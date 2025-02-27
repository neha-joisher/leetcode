class Solution:
    def rob(self, nums: List[int]) -> int:
                
        n=len(nums)
        if n==1:
            return nums[0]

        prev=nums[0]
        curr=max(nums[0],nums[1])

        for i in range(2,n):
            prev,curr=curr,max(curr,prev+nums[i]) 
        return curr
        

        ''' wrong approach- you are asked for non adjacent houses-not just even,odd 
        you can also skip a few index and mix and match
        The House Robber problem states that you cannot rob two adjacent houses, 
        but optimal combinations are not always strictly at even or odd indices.

        There could be cases where robbing some even-indexed 
        and some odd-indexed houses (skipping certain houses) yields a higher total.
        For example - 
        [2,1,1,2]- sum could be 4 but with even-odd approach- you would get 3
        sum_of_even=0
        sum_of_odd=0
        odd=1
        even=0
       
        while odd<len(nums):
            sum_of_odd+=nums[odd]
            odd+=2

        while even<len(nums):
            sum_of_even+=nums[even]
            even+=2
        return max(sum_of_odd,sum_of_even)'''
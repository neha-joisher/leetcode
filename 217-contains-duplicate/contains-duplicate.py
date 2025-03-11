class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_Nums=set(nums)
        if len(set_Nums)!=len(nums):
            return True
        return False
        
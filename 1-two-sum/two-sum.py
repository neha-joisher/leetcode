class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #[2,7,11,15] 9 
        #value index
        hashmap={} 
        for i,n in enumerate(nums):
            if target-nums[i] in hashmap:
                return [i,hashmap[target-nums[i]]]
            hashmap[n]=i


        
        
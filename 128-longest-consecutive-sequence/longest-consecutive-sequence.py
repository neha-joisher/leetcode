class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if len(nums)==0:
                return 0

            numSet=set(nums)
            maxCount = 1
            for num in numSet:
                # Check if num is the start of a sequence
                if num - 1 in numSet:
                    continue

                count=1
                j=num+1
                # Count the length of the sequence
                while j in numSet:
                    count+=1
                    j=j+1
                    maxCount = max(maxCount, count)

            return maxCount
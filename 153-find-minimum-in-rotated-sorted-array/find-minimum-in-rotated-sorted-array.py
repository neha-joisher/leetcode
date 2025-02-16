class Solution:
    def findMin(self, nums: List[int]) -> int:
        s=0
        e=len(nums)-1
        while s < e:
            mid = (e+s)// 2
            print(nums[s], nums[mid])
            if (nums[s]<=nums[mid]):
                if (nums[s]>=nums[e]):
                    s=mid+1
                else:
                    e=mid-1
            else:
                if nums[mid]<=nums[e]:
                    e=mid
        return nums[s]
        
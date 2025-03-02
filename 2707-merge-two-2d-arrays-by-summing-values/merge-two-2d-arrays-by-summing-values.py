class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=[]
        l1,l2=0,0
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1][0]==nums2[l2][0]:
                add= nums1[l1][1]+nums2[l2][1]
                res.append([nums1[l1][0],add])
                l1+=1
                l2+=1
            elif nums1[l1][0]<nums2[l2][0]:
                res.append(nums1[l1])
                l1+=1
            elif nums1[l1][0]>nums2[l2][0]:
                res.append(nums2[l2])
                l2+=1
        res.extend(nums1[l1:])
        res.extend(nums2[l2:])
        return res



        
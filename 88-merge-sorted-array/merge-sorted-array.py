class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return  # No elements to merge, return immediately
    
        p, q = 0, 0  # Pointers for nums1 and nums2
            
        while p < m + n and q < n:
            if p < m and nums1[p] <= nums2[q]:
                    p += 1
            else:
                nums1.insert(p, nums2[q])  # Insert element from nums2 into nums1
                nums1.pop()  # Remove the last element to maintain the correct size
                q += 1
                p += 1
                m += 1
        # if n==0:
        #     return
        # p,q=0,0
        # while(p<len(nums1)):
        #     if m!=0 and n!=0 and nums1[p]<=nums2[q] :
        #             p+=1
        #             m-=1
        #     else:
        #         if n==0:
        #             return
        #         nums1.insert(p,nums2[q])
        #         p+=1
        #         nums1.pop()
        #         q+=1
        #         n-=1


        
        
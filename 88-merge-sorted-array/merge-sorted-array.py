class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        p,q=0,0
        while(p<len(nums1)):
            if m!=0 and n!=0 and nums1[p]<=nums2[q] :
                    p+=1
                    m-=1
            else:
                if n==0:
                    return
                nums1.insert(p,nums2[q])
                p+=1
                nums1.pop()
                q+=1
                n-=1


        
        
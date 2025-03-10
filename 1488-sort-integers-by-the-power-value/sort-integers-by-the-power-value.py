class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # count=0
        # def power(n):
        #     nonlocal count
        #     count+=1
        #     if n==1:
        #         return count-1
        #     if n%2==0:
        #         return power(n/2)
        #     else:
        #         return power(3*n+1)
        # ans=power(3)
        # print(ans)
        res=[]
        def power(n):
            nonlocal res
            count=0
            curr=n
            while curr!=1:
                curr= (curr//2) if (curr%2==0) else ((3*curr)+1)
                count+=1
            res.append((count,n))
        for i in range(lo,hi+1):
            power(i)
        sorted_values=sorted(res)
        return sorted_values[k-1][1] 
        # ans=sorted_values[(k-1)]
        # # print(ans)
        # for i,val in res.items():
        #     print(i,val)
        #     if ans==val:
        #         return i


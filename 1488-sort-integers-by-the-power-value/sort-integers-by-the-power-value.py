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
        # res=[]
        # def power(n):
        #     nonlocal res
        #     count=0
        #     curr=n
        #     while curr!=1:
        #         curr= (curr//2) if (curr%2==0) else ((3*curr)+1)
        #         count+=1
        #     res.append((count,n))
        # for i in range(lo,hi+1):
        #     power(i)
        # sorted_values=sorted(res)
        # return sorted_values[k-1][1] 
        def collatz_steps(n, memo={}):
            if n in memo:
                return memo[n]  # Return memoized result

            if n == 1:
                return 0  # Base case: reaching 1

            next_n = n // 2 if n % 2 == 0 else 3 * n + 1  
            memo[n] = 1 + collatz_steps(next_n, memo)  # Store result in memo
            return memo[n]


        # Compute steps for each number in the range
        res = [(collatz_steps(i), i) for i in range(lo, hi + 1)]
        
        res.sort()  # Sort based on (steps, number)
            
        return res[k - 1][1]  # Get k-th smallest number



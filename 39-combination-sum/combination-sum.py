class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        n=len(candidates)
        def backtrack(i,curr_sum,):
            if curr_sum==target:
                res.append(sol.copy())
                return
            
            if curr_sum>target or i==n:
                return
            
            # don't pick i
            backtrack(i+1,curr_sum)

            #pick i
            sol.append(candidates[i])
            backtrack(i,curr_sum+candidates[i])
            sol.pop()


        backtrack(0,0)
        return res
        
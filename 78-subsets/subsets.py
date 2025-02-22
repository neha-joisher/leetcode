class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, subset = [], []

        def dfs(i):
            if i == n:
                res.append(subset.copy())
                return

            # Don't pick nums[i]
            dfs(i + 1)

            # Pick nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

        dfs(0)
        return res
        
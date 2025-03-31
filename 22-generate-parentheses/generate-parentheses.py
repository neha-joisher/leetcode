class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #Only add open if countOfOpen<n
        #Only add close if countOfClose<countOfOpen
        #basecase countOfOpen==countOfClose==n

        res=[]
        stack=[]
        def backtrack(countOfOpen,countOfClose):
            if countOfOpen==countOfClose==n:
                res.append("".join(stack))
                return
            
            if countOfOpen<n:
                stack.append("(")
                backtrack(countOfOpen+1,countOfClose)
                stack.pop()
            
            if countOfClose<countOfOpen:
                stack.append(")")
                backtrack(countOfOpen,countOfClose+1)
                stack.pop()


        backtrack(0,0)
        return res
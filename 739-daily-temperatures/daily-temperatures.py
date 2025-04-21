class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            if not stack or stack[-1][0]>temp:
                stack.append((temp,i))
            else:
                while(stack and stack[-1][0]<temp):
                    t1,j=stack.pop()
                    res[j]=i-j
                stack.append((temp,i))
        return res
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b=0
        s=1
        max_profit=0
        while s<len(prices):
            if prices[s]-prices[b]<0:
                b=s
                s+=1
            else:
                curr_profit=prices[s]-prices[b]
                max_profit=max(curr_profit,max_profit)
                s+=1
        return max_profit
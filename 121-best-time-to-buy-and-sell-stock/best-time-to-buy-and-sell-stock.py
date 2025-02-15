class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        current_profit=0
        max_profit=0
        while(sell<len(prices)):
            if(prices[sell]<prices[buy]):
                buy=sell
                sell+=1
            else:
                current_profit=prices[sell]-prices[buy]
                if(current_profit>max_profit):
                    max_profit=current_profit
                sell+=1
        print(max_profit)
        return max_profit
        
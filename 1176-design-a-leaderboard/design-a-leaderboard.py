class Leaderboard:

    def __init__(self):
        self.scorelist={}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scorelist:
            self.scorelist[playerId]+=score
        else:
            self.scorelist[playerId]=score

    def top(self, K: int) -> int:
        heap=[]
        for x in self.scorelist.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res


    def reset(self, playerId: int) -> None:
       self.scorelist[playerId]=0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
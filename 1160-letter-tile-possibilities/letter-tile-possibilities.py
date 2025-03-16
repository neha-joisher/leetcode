class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
    
        def dfs():
            total = 0
            for tile in count:
                if count[tile] > 0:
                    total += 1       # count this new sequence
                    count[tile] -= 1
                    total += dfs()   # count sequences that extend this one
                    count[tile] += 1
            return total
        
        return dfs()

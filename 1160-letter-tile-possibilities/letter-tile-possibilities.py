class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        counter = Counter(tiles)
        result = 0
        
        def backtrack():
            nonlocal result
            # Iterate over each letter that is still available
            for tile in counter:
                if counter[tile] > 0:
                    # Use this tile: it forms a new sequence (of current length + 1)
                    result += 1
                    counter[tile] -= 1
                    # Continue building the sequence with the remaining tiles
                    backtrack()
                    # Backtrack: restore the count
                    counter[tile] += 1
        
        backtrack()
        return result

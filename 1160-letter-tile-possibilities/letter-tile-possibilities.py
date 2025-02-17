class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_sequences = set()

        # Generate all permutations of all possible lengths
        for length in range(1, len(tiles) + 1):
            for perm in permutations(tiles, length):
                unique_sequences.add(perm)
        
        return len(unique_sequences)


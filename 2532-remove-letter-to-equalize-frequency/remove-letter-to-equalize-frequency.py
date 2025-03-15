class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq_count = Counter(word)  # Step 1: Count frequency of each character

        for ch in set(word):  # Try removing each unique character once
                    freq_count[ch] -= 1
                    
                    # Remove the character from dict if its count becomes 0
                    if freq_count[ch] == 0:
                        del freq_count[ch]
                    
                    # Step 2: Check if remaining frequencies are all the same
                    if len(set(freq_count.values())) == 1:
                        return True
                    
                    # Restore the original count before trying the next removal
                    freq_count[ch] += 1  

        return False

        
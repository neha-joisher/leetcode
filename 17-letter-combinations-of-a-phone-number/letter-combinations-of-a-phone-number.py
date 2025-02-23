class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # Return an empty list if the input is empty
        if not digits:
            return []

        result = []
        sol=[]

        # Backtracking function to build combinations
        def backtrack(index, sol):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                result.append("".join(sol))
                return

            # Iterate over the possible letters for the current digit
            for letter in phone_map[digits[index]]:
                sol.append(letter)        # Choose
                backtrack(index + 1, sol) # Explore
                sol.pop()                # Un-choose (backtrack)

        backtrack(0, sol)
        return result
        
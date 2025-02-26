class Solution:
    def longestPalindrome(self, s: str) -> str:

            starting_index=0
            longest_length=0

            for i in range(len(s)):
                    left,right=i,i
                    while(left>=0 and right<len(s) and s[left]==s[right]):
                        if (right-left+1>longest_length):
                            longest_length=right-left+1
                            starting_index=left
                        left-=1
                        right+=1
                    
            for i in range(len(s)):
                    left,right=i,i+1
                    while(left>=0 and right<len(s) and s[left]==s[right]):
                        if (right-left+1>longest_length):
                            longest_length=right-left+1
                            starting_index=left
                        left-=1
                        right+=1
            return s[starting_index:starting_index+longest_length]
        
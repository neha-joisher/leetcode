class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        st=0
        end=len(num)-1
        while st<=end:
            if num[st]==num[end]:
                st+=1
                end-=1
            else:
                return False
        return True
        
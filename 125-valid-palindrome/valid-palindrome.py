class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,e=0,len(s)-1
        strs=s.lower()
        def isalphanumeric(i):
            return (ord('a')<=ord(i)<=ord('z') or ord('0') <= ord(i) <= ord('9'))

        
        while(i<e):
            if (isalphanumeric(strs[i]))==False:
                i+=1
                continue
            if (isalphanumeric((strs[e])))==False:
                e-=1
                continue
            if strs[i]!=strs[e]:
                return False
            i+=1
            e-=1
        return True
        
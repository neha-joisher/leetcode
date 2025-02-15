class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i=0
        maxCount=1
        count=1
        charSet=set()
        for j in range(len(s)):
            print(s[j],s[j] in charSet)
            if s[j] in charSet:
                print(s[i],s[j],s[i]!=s[j])
                while s[i]!=s[j]:
                    charSet.remove(s[i])
                    i+=1
                charSet.remove(s[i])
                i+=1
            charSet.add(s[j])
            if len(charSet)>maxCount:
                maxCount=len(charSet)
            print(maxCount)
        return maxCount
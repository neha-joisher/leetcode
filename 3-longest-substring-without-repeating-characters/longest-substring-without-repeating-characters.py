class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        hashset=set()
        res=0
        for end in range(len(s)):
            while s[end] in hashset:
                hashset.remove(s[start])
                start+=1
            hashset.add(s[end])
            res=max(res,end-start+1)
            print(hashset)
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        i=j=0
        max_len=1
        hashmap={}

        while(j<len(s)):

            hashmap[s[j]]=1+hashmap.get(s[j],0)

            max_freq=max(hashmap.values())
            if ((j-i)+1)-max_freq<=k:
                max_len=max(max_len,((j-i)+1))
                j+=1
            else:
                hashmap[s[i]]-=1
                i+=1
                j+=1
        return max_len


        
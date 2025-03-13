class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        i=j=0
        max_len=1
        hashmap={}

        def get_max_freq():
            count=int(max(hashmap.values()))
            return count

        while(j<len(s)):
            if s[j] in hashmap:
                hashmap[s[j]]=hashmap[s[j]]+1
            else:
                hashmap[s[j]]=1

            max_freq=get_max_freq()
            if ((j-i)+1)-max_freq<=k:
                max_len=max(max_len,((j-i)+1))
                j+=1
            else:
                hashmap[s[i]]=hashmap[s[i]]-1
                i+=1
                j+=1
        return max_len

        
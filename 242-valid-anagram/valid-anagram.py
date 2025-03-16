class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_Counter_S=Counter(s)
        freq_Counter_T=Counter(t)
        return freq_Counter_S==freq_Counter_T

        # hashmap_s={}
        # hashmap_t={}

        # def get_count(hashmap,st):
        #     for x in st:
        #         if x in hashmap:
        #             hashmap[x]=hashmap[x]+1
        #         else:
        #             hashmap[x]=1
        #     return hashmap
        # hashmap_s= get_count(hashmap_s,s)
        # hashmap_t= get_count(hashmap_t,t)

        # if hashmap_s==hashmap_t:
        #     return True
        # else:
        #     return False
        
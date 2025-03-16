class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for word in strs:
            freq_arr=[0]*26
            for char in word:
                freq_arr[ord(char)-ord('a')]+=1
            hashmap[tuple(freq_arr)].append(word)
        return list(hashmap.values())
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize empty buckets for each freq
        arr=[[] for i in range(len(nums)+1)]

        #get the freq count
        freq_counter=Counter(nums)

        for key,value in freq_counter.items():
            arr[value].append(key)


        res=[]
        for i in range(len(nums),0,-1):
            # if arr[i]==[]:
            #     continue 
            for num in arr[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
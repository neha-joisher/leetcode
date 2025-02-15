class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={"]":"[",")":"(","}":"{"}
        arr=[]
        i=0
        while i<len(s):
            if s[i] not in hashmap:
                arr.append(s[i])
            else:
                if len(arr)!=0 and arr[len(arr)-1]==hashmap[s[i]] :
                    arr.pop()
                else: 
                    return False
            i+=1
        if len(arr)==0:
            return True
        else:
            return False

        
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        freqMap1=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if s2[i] in freqMap1:
                freqMap2=Counter(s2[i:i+len(s1)])
                if freqMap1==freqMap2:
                    return True
        return False

        

        
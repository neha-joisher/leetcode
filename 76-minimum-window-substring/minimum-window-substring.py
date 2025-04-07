class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t)>len(s):
            return ''
        freq_Counter_t=Counter(t)
        need=len(freq_Counter_t)
        have=0
        freq_Counter_s={}
        st=e=0
        min_substring=''
        min_length=float('inf')
        while e<len(s):#or window is valid
            if s[e] in freq_Counter_t:
                freq_Counter_s[s[e]]=freq_Counter_s.get(s[e],0)+1
                if freq_Counter_s[s[e]]==freq_Counter_t[s[e]]:
                    have+=1
            while have==need:#window is valid
                if e-st+1<min_length:
                    min_length=e-st+1
                    min_substring=s[st:e+1]
                if s[st] in freq_Counter_t:
                    freq_Counter_s[s[st]] -= 1
                    if freq_Counter_s[s[st]]<freq_Counter_t[s[st]]:
                        have-=1
                st += 1
            e+=1
        return min_substring

        # if len(t)>len(s):
        #     return ''
        # freq_Counter_t=Counter(t)
        # freq_Counter_s={}
        # st=e=0
        # min_substring=''
        # min_length=float('inf')
        # def window_is_valid():
        #     for ch in freq_Counter_t:
        #         if freq_Counter_s.get(ch, 0) < freq_Counter_t[ch]:
        #             return False
        #     return True
        # while e<len(s):#or window is valid
        #     if s[e] in freq_Counter_t:
        #         freq_Counter_s[s[e]]=freq_Counter_s.get(s[e],0)+1
        #     while window_is_valid():#window is valid
        #         if e-st+1<min_length:
        #             min_length=e-st+1
        #             min_substring=s[st:e+1]
        #         if s[st] in freq_Counter_t:
        #             freq_Counter_s[s[st]] -= 1
        #         st += 1
        #     e+=1
        # return min_substring
        
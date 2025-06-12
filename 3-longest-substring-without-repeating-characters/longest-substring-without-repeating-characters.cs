public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var uniqueCharSet=new HashSet<char>();
        int maxLen=0;
        int st=0;
        int end=0;

        while(end<s.Length){
            while(uniqueCharSet.Contains(s[end])){
                uniqueCharSet.Remove(s[st]);
                st++;
            }
            uniqueCharSet.Add(s[end]);
            maxLen=Math.Max(maxLen,end-st+1);
            end++;
        }
        return maxLen;

    }
}
public class Solution {
    public int CharacterReplacement(string s, int k) {
        var freqMap=new Dictionary<char,int>();
        int start=0;
        int end=0;
        int maxLength=0;
        while(end<s.Length){
            if(freqMap.ContainsKey(s[end])){
                freqMap[s[end]]++;
            }else{
                freqMap[s[end]]=1;
            }
            var mostFreqCharCount=freqMap.OrderByDescending(kvp=>kvp.Value).Select(kvp=>kvp.Value).First();
            if((end-start+1)-mostFreqCharCount>k){
                freqMap[s[start]]--;
                start++;
            }
            maxLength=Math.Max(maxLength,(end-start+1));
            end++;
        }
        return maxLength; 
    }
}
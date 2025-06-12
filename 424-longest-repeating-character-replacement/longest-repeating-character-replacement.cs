public class Solution {
    public int CharacterReplacement(string s, int k) {
        var freqMap=new Dictionary<char,int>();
        int start=0, end=0, maxLength=0, mostFreqCharCount=0;
        while(end<s.Length){
            // if(freqMap.ContainsKey(s[end])){
            //     freqMap[s[end]]++;
            // }else{
            //     freqMap[s[end]]=1;
            // }
            if (!freqMap.ContainsKey(s[end])) {
                freqMap[s[end]] = 0;
            }
            freqMap[s[end]]++;
            mostFreqCharCount=Math.Max(mostFreqCharCount,freqMap[s[end]]);
            // var mostFreqCharCount=freqMap.OrderByDescending(kvp=>kvp.Value).Select(kvp=>kvp.Value).First();
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

public class Solution {
    public bool IsPalindrome(string s) {
        int start=0;
        int end=s.Length-1;

        s=s.ToLower();
        while(start<end){
            Console.WriteLine(s[start] + " " + s[end]);
            if(isAlphaNumeric(s[start])){
                if(isAlphaNumeric(s[end])){
                    if(s[start]==s[end]){
                        start++;
                        end--;
                    }else{
                        return false;
                    }
                }else{
                    end--;
                }
            }else{
                start++;
            }
        }
        return true;
    }

    public bool isAlphaNumeric(char c){
        //chained operation not allowed ('a'<=c<='z')
        // if(('a'<=c<='z') ||  ('A'<=c<='Z') || ('0'<=c<='9')){
        //     return true;
        // }

        //return char.IsLetterOrDigit(c)
        if((c>='a' && c<='z') || (c>='A' && c<='Z') || (c>='0' && c<='9')){
            return true;
        }
        return false;
    }
}
public class Solution {

    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        var current = new StringBuilder();

        void Backtrack(int open, int close) {
            if (open == n && close == n) {
                result.Add(current.ToString());
                return;
            }

            if (open < n) {
                current.Append('(');
                Backtrack(open + 1, close);
                current.Length--; // backtrack
            }

            if (close < open) {
                current.Append(')');
                Backtrack(open, close + 1);
                current.Length--; // backtrack
            }
        }

        Backtrack(0, 0);
        return result;
    }
}

    //     int noOfOpen=0, noOfClose=0;
    //     var stack=new Stack<string>();
    //     var sol=new List<string>();
        
    //     void backtrack( int noOfOpen, int noOfClose){

    //         if(noOfOpen==n && noOfClose==n){
    //             sol.Add(string.Join("", stack.Reverse())); 
    //             return;
    //         }

    //         //1.Open->Till i reach n
    //         if(noOfOpen<n){
    //             stack.Push("(");
    //             backtrack(noOfOpen+1, noOfClose,stack);
    //             stack.Pop()
    //         }

    //         //2. Close if close<open
    //         if(noOfClose<noOfOpen){
    //             stack.Push(")");
    //             backtrack(noOfOpen, noOfClose+1,stack);
    //             stack.Pop();
    //         }
    //     }

    //     backtrack(0,0);
    //    return sol;
    // }
// }
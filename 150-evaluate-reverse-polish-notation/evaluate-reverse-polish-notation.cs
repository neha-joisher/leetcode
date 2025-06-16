public class Solution {
    public int EvalRPN(string[] tokens) {
        var operators = new HashSet<string> { "+", "-", "*", "/" };
        var stack = new Stack<int>();

        foreach (string token in tokens) {
            if (!operators.Contains(token)) {
                stack.Push(int.Parse(token));
            } else {
                int input2 = stack.Pop();
                int input1 = stack.Pop();
                int res = 0;

                switch (token) {
                    case "+":
                        res = input1 + input2;
                        break;
                    case "-":
                        res = input1 - input2;
                        break;
                    case "*":
                        res = input1 * input2;
                        break;
                    case "/":
                        res = input1 / input2;
                        break;
                }

                stack.Push(res);
            }
        }

        return stack.Pop();
    }
}

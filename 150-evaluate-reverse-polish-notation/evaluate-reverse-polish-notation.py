class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+', '-', '*', '/']
        stack=[]

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                operand2=stack.pop()
                operand1=stack.pop()
                if t=='+':
                    ans=operand1 + operand2
                elif t=='-':
                    ans=operand1 - operand2
                elif t=='*':
                    ans=operand1 * operand2
                elif t=='/':
                    ans=int((operand1) / operand2)
                stack.append(ans)
        print(stack)
        return stack[-1]
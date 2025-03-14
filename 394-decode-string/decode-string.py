class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
            else:
                sub_string=''
                while stack[-1]!='[':
                    sub_string=stack.pop()+sub_string
                stack.pop()
                digit=''
                while stack and stack[-1].isdigit():
                    digit=stack.pop()+digit
                stack.append(int(digit)*sub_string)
        return "".join(stack)

            
        

            
            
        
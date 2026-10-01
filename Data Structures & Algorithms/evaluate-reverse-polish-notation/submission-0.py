class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands={
            '+': lambda a,b:a+b,
            '-': lambda a,b:a-b,
            '*': lambda a,b:a*b,
            '/': lambda a,b:int(a / b)
        }
        stack=[]
        i=0
        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                b=stack.pop()
                a=stack.pop()
                result= operands[tokens[i]](a,b)
                stack.append(result)
        return stack[0]
            






        
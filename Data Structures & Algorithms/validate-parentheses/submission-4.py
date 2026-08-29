class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            '(':')',
            '{':'}',
            '[':']'
        }
        closing = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack =[]
        for i in s:
            if i in valid:
                stack.append(i)
            elif i in closing:
                if len(stack)>0 and closing[i]==stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0
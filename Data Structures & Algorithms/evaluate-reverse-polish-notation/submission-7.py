class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        
        for i in tokens:
            
            if i == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2)  + int(val1))
            elif i == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2)  - int(val1))
            elif i == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                res = int(val2) / int(val1)
                stack.append(res)
            elif i == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                res = int(val2) * int(val1)
                stack.append(res)
            else:
                stack.append(i)
        
        return int(stack.pop())


        
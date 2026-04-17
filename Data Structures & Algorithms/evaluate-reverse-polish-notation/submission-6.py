class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arthemetics = ['+', '-', '*', '/']
        value = 0

        for i in tokens:
            if i not in arthemetics:
                stack.append(i)
         
            else:
                if len(stack) >= 2:

                    value1 = stack.pop()
                    value1 = int(value1)
                    value2 = stack.pop()
                    value2 = int(value2)
                    if i == "+":
                        value = value2 + value1
                        stack.append(value)
                    elif i == "-":
                        value = value2 - value1
                        stack.append(value)
                    elif i == "*":
                        value = value2 * value1
                        stack.append(value)
                    else:
                        value = value2 / value1
                        stack.append(value)

        return int(stack.pop())
            

                    

        
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")" : "(", "]": "[", "}" : "{"}

        stack= []
        for bracket in s:
            if bracket in dic.values():
                stack.append(bracket)
            
            else:
                if not stack:
                    return False

                val = stack.pop()

                if val != dic[bracket]:
                    return False
                
        return len(stack) == 0
        

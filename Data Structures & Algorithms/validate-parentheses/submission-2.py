class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "}":"{", "]":"["}

        stack = []

        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic.keys():
                if not stack:
                    return False
                val = stack.pop()
                if val != dic[i]:
                    return False

        return len(stack) == 0 




                
                

            
        
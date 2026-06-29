class Solution:
    def isValid(self, s: str) -> bool:

        d = {")": "(", "]":"[" , "}": "{"}
        openings = [")", ']', "}"]

        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
                print(stack)
            elif i in d.keys():
                if stack and stack[-1] == d[i]:
                    print(stack)
                    stack.pop()
                else:
                    return False

    
        return len(stack) == 0 




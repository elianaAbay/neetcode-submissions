class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 0, 1

        #the time complectiy for this problem, o(n), orginally though of o(2^n)
        for i in range(n):
            temp = l + r 
            l = r 
            r = temp 

        return temp


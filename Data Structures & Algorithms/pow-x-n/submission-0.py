class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        while n !=0:
            if n < 0:
    
                res = res/x
                n = n + 1
            if n > 0:

                res = res*x
                n = n-1
        return res


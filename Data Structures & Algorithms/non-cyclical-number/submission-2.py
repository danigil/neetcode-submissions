class Solution:
    def isHappy(self, n: int) -> bool:

        def _calc(n:int) -> int:
            s=0
            while n>0:
                s += ((n%10)**2)
                n=n//10
            return s

        s=set([n])
        curr=n
        while True:
            res=_calc(curr)
            if res==1:
                return True
            if res in s:
                return False
            s.add(res)
            curr=res
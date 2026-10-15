class Solution:
    def fib(self, n:int) -> int:
        if n<=1:
            return n
        elif n==2:
            return 2
        else:
            return self.fib(n-1) + self.fib(n-2)
    def climbStairs(self, n: int) -> int:
        base=[1,1,2,3]
        if n<=3:
            return base[n]
        sols=base+[None]*(n-3)
        for i in range(4,n+1):
            curr=sols[i-1]+sols[i-2]
            sols[i]=curr
        return sols[-1]
        # return self.fib(n)
        

        # sols=[None]*n
        # sols[0]=1
        # sols[1]=2

        # # def solve()
        # curr=2
        # while curr<=n:
        #     prev=curr-2
        #     prev_sol=sols[prev]


        
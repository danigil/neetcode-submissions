class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        i=2
        while i <= len(cost): 
            one=dp[i-1]+cost[i-1]
            two=dp[i-2]+cost[i-2]
            dp[i]=min(one,two)
            i+=1
        return dp[-1]
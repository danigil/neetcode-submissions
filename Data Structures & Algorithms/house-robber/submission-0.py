class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        ret = 0
        for i,n in enumerate(nums):
            dp[i+2] = max(n+dp[i], dp[i+1])
            ret = max(ret, dp[i+2])
        
        return ret
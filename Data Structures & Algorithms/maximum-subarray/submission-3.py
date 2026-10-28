class Solution:
    def cumsum(self, nums: List[int]) -> List[int]:
        s=0
        ret=[None]*len(nums)
        for i,n in enumerate(nums):
            ret[i]=s+n
            s+=n
        return ret

    def max_oneside(self, nums: List[int]) -> int:
        cumsum = self.cumsum(nums)
        highest = max(cumsum)
        highest_i = cumsum.index(highest)
        if highest_i > 0:
            smallest = min(cumsum[:highest_i])
        else:
            smallest = 0

        return max(highest, highest - smallest)

    def maxSubArray(self, nums: List[int]) -> int:
        return max(self.max_oneside(nums), self.max_oneside(list(reversed(nums))))
        
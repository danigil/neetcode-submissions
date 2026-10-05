class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {v:i for i,v in enumerate(nums)}
        i=0
        for i1,v in enumerate(nums):
            if (target - v) in d and (i2:=d[target-v]) != i1:
                i2 = d[target-v]
                return list(sorted((i1,i2)))

        
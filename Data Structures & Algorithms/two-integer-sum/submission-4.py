import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = np.array(nums)
        nums_idxs = np.argsort(nums, stable=True, descending=False)
        nums = nums[nums_idxs]

        l = 0
        r = len(nums)-1
        while 0 <= l < r <= len(nums)-1:
            res = nums[l] + nums[r]
            # print(res)
            if res == target:
                return list(sorted([nums_idxs[l], nums_idxs[r]]))
            else:
                if res > target:
                    r-=1
                else:
                    l+=1
        
        return [0,0]
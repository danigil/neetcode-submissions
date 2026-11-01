class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        onestep=max(nums[0], nums[1])
        twostep=nums[0]

        for i, n in enumerate(nums[2:]):
            tmp = onestep

            if n + twostep > onestep:
                onestep = n + twostep
            else:
                pass 
            twostep=tmp

        return max(onestep, twostep)

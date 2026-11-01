class Solution:
    def rob1(self, nums: List[int]) -> int:
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

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob0 = self.rob1(nums[:-1])
        robn = self.rob1(nums[1:])

        return max(rob0, robn)
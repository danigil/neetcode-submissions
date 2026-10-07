from copy import deepcopy
class Solution:
    def rolling_product(self, nums: List[int]) -> List[int]:
        ret = deepcopy(nums)
        for i,n in enumerate(ret):
            if i==0:
                continue
            else:
                ret[i]*=ret[i-1]
        return ret

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_rp = self.rolling_product(nums)
        nums_rp_r = list(reversed(self.rolling_product(list(reversed(nums)))))
        # print(nums_rp)
        # print(nums_rp_r)

        ret = [None]*len(nums)
        for i,_ in enumerate(nums):
            if i==0:
                ret[i]=nums_rp_r[i+1]
            elif i == (len(nums)-1):
                ret[i]=nums_rp[i-1]
            else:
                ret[i]=nums_rp[i-1] * nums_rp_r[i+1]
        return ret
            

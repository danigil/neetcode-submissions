class Solution:
    def findMin(self, nums: List[int]) -> int:
        # def find(nums: List[int], l,r):
        #     l = l%len(nums)
        #     r = r % len(nums)
        #     if nums[l] < nums[r] and l==r+1:
        #         return nums[l]
            
        #     else:
        #         if nums[l] < nums[r]:
        #             return find(nums, l, )
        #         else:

        l=0
        r=len(nums)-1

        while l < r:
            mid=(l+r)//2
            if nums[mid] < nums[r]:
                r=mid
            else:
                l=mid+1
        
        return nums[l]


            

        
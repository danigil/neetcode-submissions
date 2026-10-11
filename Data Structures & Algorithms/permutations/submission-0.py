class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(index, path):
            if index==len(nums):
                ret.append(path[:])
                return

            for i in range(len(nums)):
                if path[i] is not None:
                    continue

                path[i]=nums[index]
                backtrack(index+1,path)
                path[i]=None
            # # include index
            # path.append(nums[index])
            # backtrack(index+1, path)
            # path.pop()

            # # don't include index
            # backtrack(index+1, path)

        backtrack(0, [None]*len(nums))
        return ret
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(index, path):
            if index==len(nums):
                ret.append(path[:])
                return

            # # include index
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            # # don't include index
            backtrack(index+1, path)

        backtrack(0, [])
        return ret
        
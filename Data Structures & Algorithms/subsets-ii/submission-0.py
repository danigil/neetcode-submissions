class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        def backtrack(index, path):
            if path in ret:
                return
            if index == len(nums):
                ret.add(path)
                return

            # path.append(nums[index])
            backtrack(index+1, path + (nums[index],))

            # path.pop()
            backtrack(index+1, path)

        backtrack(0, tuple())
        ret = [list(x) for x in ret]
        return ret
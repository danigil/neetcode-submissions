class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret=[]
        
        def backtrack(index,path):
            s=sum(path)
            if s==target:
                ret.append(path[:])
                return

            if s>target:
                return

            for i, num in enumerate(nums):
                if i>=index:
                    path.append(num)
                    backtrack(i, path)
                    path.pop()
            

        backtrack(0, [])

        return ret
        
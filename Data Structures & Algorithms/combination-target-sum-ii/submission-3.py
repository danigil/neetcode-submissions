class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        candidates=list(sorted(candidates))
        
        def backtrack(index,path,s):
            # s=sum(path)
            if s==target:
                ret.append(path[:])
                return

            if s>target:
                return

            for i in range(index, len(candidates)):
                if  i>index and candidates[i] == candidates[i - 1]:
                    continue

                if s + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i+1, path, s+ candidates[i])
                path.pop()
            

        backtrack(0, [], 0)

        return ret
        
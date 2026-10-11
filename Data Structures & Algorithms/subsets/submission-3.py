class Solution:
    def copy_arr(self, nums: List[int], except_i=-1) -> List[int]:
        return tuple(n for i,n in enumerate(nums) if i!=except_i)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q=[self.copy_arr(nums)]
        s=set()
        while q:
            curr=q.pop()
            # ret.append(curr)
            s.add(curr)
            for i in range(len(curr)):
                curr_add=self.copy_arr(curr, i)
                if curr_add not in s:
                    q.append(curr_add)
        ret=[list(t) for t in s]

        return ret
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if len(temperatures)==0:

        stack=[]
        ret=[0]*len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                _,j=stack.pop()
                ret[j]=i-j
            stack.append((temp,i))

        return ret
        
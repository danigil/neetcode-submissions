class Solution:
    def water(self, i: int) -> int:
        if i == 0 or i == len(self.height) - 1:
            return 0
        
        ret = 0
        center = self.height[i]
        # left_max = max(self.height[0:i])
        left_max = self.leftmax[i]
        # right_max = max(self.height[i+1:])
        right_max = self.rightmax[i]

        return max(0, min(left_max, right_max)-center)

    def calc_cummax(self, l: List[int]) -> List[int]:
        if len(l) < 1:
            return []
        ret = [l[0]] * len(l)
        ret[len(l)-1] = max(l)
        for i, h in enumerate(l):
            if i == 0:
                continue
            ret[i] = max(h, ret[i-1])
        
        return ret

    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        ret = 0
        self.height = height
        self.leftmax = self.calc_cummax(height)
        self.rightmax = list(reversed(self.calc_cummax(list(reversed(height)))))

        # print(self.leftmax)
        # print(self.rightmax)

        for i, h in enumerate(height):
            ret += self.water(i)
        return ret
        
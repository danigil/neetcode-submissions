class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        max_a = 0
        while 0 <= l < r < len(heights):
            a = min(heights[l], heights[r])*(r-l)
            max_a = max(max_a, a)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_a
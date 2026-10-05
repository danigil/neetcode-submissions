from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        mc = c.most_common(k)
        return [t[0] for t in mc]
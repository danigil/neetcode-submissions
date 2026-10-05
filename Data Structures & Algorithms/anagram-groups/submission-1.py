from collections import Counter, defaultdict
from itertools import groupby

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = [None] * len(strs)
        for i,s in enumerate(strs):
            c = Counter(s)
            c.s = s
            counters[i] = c
        # counters = sorted(counters)
        # print(counters)

        # groupby bundles consecutive equal elements together
        # grouped = [list([g.s for g in group]) for key, group in groupby(counters)]

        # print(grouped)
        # Group items by their own value
        grouped = defaultdict(list)
        for item in counters:
            grouped[frozenset(item.items())].append(item)

        ret = []
        for k,v in grouped.items():
            ret.append([a.s for a in v])

        # print(dict(grouped))

        return ret
        
        
        
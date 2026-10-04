from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for c in s:
        #     if c not in t:
        #         return False

        char_counts_1 = Counter(s)
        char_counts_2 = Counter(t)
        return char_counts_1 == char_counts_2
class Solution:
    def make_counter_dict(self, s:str) -> dict:
        d = {}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        return d

    def is_counter_dict_equal(self, d1, d2) -> bool:
        for k1,v1 in d1.items():
            v2 = d2.get(k1)
            if v2 is None or v1!=v2:
                return False

        for k2,v2 in d2.items():
            v1 = d1.get(k2)
            if v1 is None or v2!=v1:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        winsize = len(s1)
        i=0

        d1 = self.make_counter_dict(s1)
        # d2 = self.make_counter_dict(s2)

        while 0 <= i <= len(s2)-winsize:
            d = self.make_counter_dict(s2[i:i+winsize])
            if self.is_counter_dict_equal(d1,d):
                return True
            i+=1

        return False



        
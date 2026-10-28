class Solution:
    

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        def get_interval_i(i):
            return intervals[i][0], intervals[i][1]

        intervals.sort(key=lambda interval: interval[0])
        curr_i=0
        curr_s, curr_e = get_interval_i(curr_i)
        next_i=1

        ret = []

        while next_i < len(intervals):
            next_s, next_e = get_interval_i(next_i)

            if next_s <= curr_e:
                curr_e = max(curr_e, next_e)
                next_i += 1
            else:
                ret.append([curr_s, curr_e])
                curr_i=next_i
                curr_s, curr_e = get_interval_i(curr_i)
                next_i+=1

        ret.append([curr_s, curr_e])

        return ret
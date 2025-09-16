class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval[0])
        pe = intervals[0][1]
        removed_count = 0
        for i in range(1, len(intervals)):
            cs, ce = intervals[i][0], intervals[i][1]
            if cs < pe:  # overlap
                removed_count += 1
                pe = min(pe, ce)
            else:
                pe = ce
        return removed_count

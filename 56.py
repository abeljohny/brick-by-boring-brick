class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            cs, ce = intervals[i][0], intervals[i][1]
            lms, lme = output[-1][0], output[-1][1]
            if cs <= lme:
                output[-1][1] = max(ce, lme)
            else:
                output.append(intervals[i])

        return output
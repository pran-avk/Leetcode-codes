class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        prev_end=float('-inf')
        rem=0
        for start,end in intervals:
            if start>=prev_end:
                prev_end=end
            else:
                rem+=1
        return rem
        
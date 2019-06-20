class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        The idea is to sort the intervals by their starting points.  
        Then, we take the first interval and compare its end with the next intervals starts. 
        As long as they overlap, we update the end to be the max end of the overlapping intervals. 
        Once we find a non overlapping interval, we can add the previous "extended" interval and start over.
        Sorting takes O(n log(n)) and merging the intervals takes O(n). So, the resulting algorithm takes O(nlog(n)).
        """
        
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        new_interval = intervals[0]
        res.append(new_interval)
        
        for interval in intervals:
            if interval[0] <= new_interval[1]:
                new_interval[1] = max(new_interval[1], interval[1])
            else:
                new_interval = interval
                res.append(new_interval)
        
        return res

#973
from heapq import heappush, heappop

class Solution(object):
    def kClosest(self, points, n):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = lambda x : points[x][0]**2 + points[x][1]**2
        
        heap = []
        
        for i in range(len(points)) :
            heappush(heap, (-dist(i), points[i]))
            
            if len(heap) > n :
                heappop(heap)
        
        return [heappop(heap)[1] for i in range(n)]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key= lambda pair: sqrt(pair[0]**2+pair[1]**2))
        return points[:k]


    
    
from heapq import heapify, heappush, heappop
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return math.sqrt(x**2+y**2)
        
        points = [[dist(x,y), [x,y]] for x, y in points]
        heapify(points)
        
        ans = []
        
        for _ in range(k):
            d, coords = heappop(points)
            ans.append(coords)
            
        return ans    

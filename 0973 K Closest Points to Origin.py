class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key= lambda pair: sqrt(pair[0]**2+pair[1]**2))
        return points[:k]

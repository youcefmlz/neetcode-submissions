class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        Heap = []

        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(Heap , [-dist , x, y])

        heapq.heapify(Heap)

        while len(Heap) > k:
            heapq.heappop(Heap)
        return [[x[1],x[2]] for x in Heap]


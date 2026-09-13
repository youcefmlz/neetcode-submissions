class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap , [-dist , x, y])

        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        # print(minHeap)
        return [[x[1],x[2]] for x in minHeap]


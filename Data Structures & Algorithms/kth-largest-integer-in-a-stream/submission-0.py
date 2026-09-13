class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap , self.k = nums , k
        #turn the nums array into min Heap:
        heapq.heapify(self.minHeap)
        #make sure the size of our heap is k
        while (len(self.minHeap) > k):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # we will just add the value to the min heap without caring if it 
        # is big or small. after adding it we pop the smallest value to keep the size k 
        heapq.heappush(self.minHeap , val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0] #the min elements would be always index 0 
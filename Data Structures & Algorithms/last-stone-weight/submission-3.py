class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
	        stones[i] = -stones[i]
        heapq.heapify(stones)

        while(len(stones) > 1):
            
            x1 = - heapq.heappop(stones)
            x2 = - heapq.heappop(stones)

            if x1 == x2:
                continue
            else:
                heapq.heappush(stones , -(x1 - x2) )
        if len(stones) ==1 :
            return -stones[0]
        else: return 0
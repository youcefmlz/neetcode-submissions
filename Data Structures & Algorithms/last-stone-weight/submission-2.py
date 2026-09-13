class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        for i in range(len(stones)):
	        stones[i] = -stones[i]
        heapq.heapify(stones)
        print(stones)
        while(len(stones) > 1):
            # print(f"stones inside the while loop {stones}")
            
            x1 = - heapq.heappop(stones)
            # print(f"x1 {x1}")
            x2 = - heapq.heappop(stones)
            # print(f"x2 {x2}")

            if x1 == x2:
                # print("inside equal")
                continue
            else:
                # print(f"inside else :{x1-x2}" )
                heapq.heappush(stones , -(x1 - x2) )
        if len(stones) ==1 :
            return -stones[0]
        else: return 0
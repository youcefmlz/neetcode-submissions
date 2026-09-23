class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num]+=1
        
        res = sorted(dic.keys(), key = dic.get, reverse = True)
    
        return res[0:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(0,len(nums)):
            hashMap[nums[i]]=hashMap.get(nums[i],0) +1
        sorted_hash_map = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        returnList =[]
        for i, key in enumerate(sorted_hash_map.keys()):
            if i < k:
                returnList.append(key)
        return returnList
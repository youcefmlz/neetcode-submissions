class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force:
        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if(numbers[i]+numbers[j]==target):
        #             return [i+1,j+1]

        #. Hash Map 
        hashmap = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in hashmap:
                firstIndex = hashmap[difference]
                return [firstIndex+1 ,i+1 ]
            hashmap[numbers[i]]= i
        
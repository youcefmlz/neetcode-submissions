class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #. Brute force - time complex : O(n^2) space complex : O(1)
        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if(numbers[i]+numbers[j]==target):
        #             return [i+1,j+1]
        # return []
        #. Hash Map    - time complex : O(n) space complex : O(n)
        # hashmap = {}
        # for i in range(len(numbers)):
        #     difference = target - numbers[i]
        #     if difference in hashmap:
        #         firstIndex = hashmap[difference]
        #         return [firstIndex+1 ,i+1 ]
        #     hashmap[numbers[i]]= i
        
        #. Two Pointers 
        frontPointer = 0
        endPointer = len(numbers)-1
        while frontPointer < endPointer:
            if numbers[frontPointer]+numbers[endPointer] ==target:
                return [frontPointer+1 , endPointer+1]
            elif numbers[frontPointer]+numbers[endPointer] > target:
                endPointer -= 1
                continue
            elif numbers[frontPointer]+numbers[endPointer] < target:
                frontPointer+=1
                continue
        return []



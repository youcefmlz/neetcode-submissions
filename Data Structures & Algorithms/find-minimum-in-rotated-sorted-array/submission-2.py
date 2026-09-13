class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        right = len(nums)-1
        left =0

        while(left <= right):
            if(nums[left]< nums[right]):
                res = min(res , nums[left])
                break


            med = int((left+right)//2)
            res = min(res , nums[med])

            if(nums[med]>= nums[right]): #go right
                left = med +1
            else:  #go left 
                right = med - 1

        return res 

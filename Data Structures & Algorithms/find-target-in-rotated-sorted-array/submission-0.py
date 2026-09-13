class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1

        while(l <= r): #less than or equal in case of an array : [1]
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            #left sorted portion of the array: 
            if nums[mid]>= nums[l]:  #the middle value is greater than the left value
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            #right sorted portion of the array: 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
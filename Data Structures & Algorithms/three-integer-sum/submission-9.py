class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        nums.sort()


        for i in range(len(nums)):
            print(f'i is : {nums[i]}')
            if(i>0 and nums[i]==nums[i-1]):
                continue
            print(f'i after of state is : {nums[i]}')
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l]+nums[r] +nums[i]>0 :
                    r -=1
                elif nums[l]+nums[r] +nums[i]<0 :
                    l +=1
                else:
                    return_list.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return return_list






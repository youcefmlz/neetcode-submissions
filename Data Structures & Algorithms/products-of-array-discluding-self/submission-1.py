class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = n * [0]
        prefix = n * [0]
        postfix = n * [0]

        for i in range(len(nums)):
            if(i==0):
                prefix[i]=nums[i]
            else:
                prefix[i]=prefix[i-1]*nums[i]

        for i in range(len(nums)-1,-1,-1):
            if(i == len(nums)-1):
                postfix[i]=nums[i]
            else:
                postfix[i]=  postfix[i+1] *nums[i]
        
        for i in range(len(nums)):
            if(i==0):
                result[i]=postfix[i+1]
            elif (i==len(nums)-1):
                result[i]=prefix[i-1]
            else:
                result[i]=prefix[i-1] * postfix[i+1]
        
        return result



        

        
                    
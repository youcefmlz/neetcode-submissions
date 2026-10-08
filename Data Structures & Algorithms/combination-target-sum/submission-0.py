class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):

            #stop if the sum already exceeds the target
            #or run out of numbers
            if i>=len(nums) or sum(subset)>target:
                return

            #found a valid combination
            if sum(subset) == target: 
                res.append(subset.copy())
                return
            #choice01: include nums[i]
            subset.append(nums[i])


            dfs(i)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
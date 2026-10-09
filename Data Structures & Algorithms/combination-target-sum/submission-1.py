class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):

            #stop if the sum already exceeds the target
            #or run out of numbers
            if i>=len(nums) or total>target:
                return

            #found a valid combination
            if total == target: 
                res.append(subset.copy())
                return
            #choice01: include nums[i]
            subset.append(nums[i])


            dfs(i, total + nums[i])

            subset.pop()
            dfs(i+1, total)
        
        dfs(0, 0 )
        return res
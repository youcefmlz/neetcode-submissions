class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtracking(index):

            if index>=len(nums): #this is the end of tree - leaf 
                res.append(subset.copy()) #add combination to the result array
                return

            #choice01: include nums[index]
            subset.append(nums[index])
            backtracking(index+1)

            #undo choice01
            subset.pop()

            #choice02: exclude nums[index]
            backtracking(index+1)
        
        backtracking(0)
        return res


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the row :
        top, bottom = 0, len(matrix)-1

        while(top<=bottom):
            row = (top+bottom)//2

            if matrix[row][0] > target:
                bottom = row -1
            elif  matrix[row][-1] < target:
                top = row +1
            else:
                break

        
        l, r =0, len(matrix[row])-1
        while(l<=r):
            mid2=(l+r)//2
            if matrix[row][mid2]==target:
                return True
            elif matrix[row][mid2]>target:
                r=mid2 -1
            else:
                l=mid2+1
        
        return False
                

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search2d(matrix: List[List[int]], l,r,target) -> bool:
            if l >= r:
                return False

            # if not matrix or not matrix[0]:
            #     return False
            m,n = len(matrix), len(matrix[0])

            middle = (l+r)//2
            i,j=divmod(middle, n)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return search2d(matrix, l, middle, target)
            else:
                return search2d(matrix, middle+1, r,target)
        m,n = len(matrix), len(matrix[0])
        return search2d(matrix, 0, m*n, target)

            

            


        
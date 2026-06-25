class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m,n = len(matrix),len(matrix[0])

        
        def find(x,y):
            if x>=m or y>=n:
                return False
            if target==matrix[x][y]:
                return True

            if x == m - 1:
                return find(x, y + 1)
                
            elif target>matrix[x][y] and target<matrix[x+1][y]:
                return find(x,y+1)
            else:
                return find(x+1,y)

        return find(0,0)
            

        

    
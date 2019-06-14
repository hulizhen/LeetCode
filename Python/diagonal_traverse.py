class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = 0
        result = [0] * m * n
        for i in range(m * n):
            print(i)
            result[i] = matrix[row][col]
            delta = 1 if (row + col) % 2 == 0 else -1
            row -= delta
            col += delta

            if row >= m:
                row -= 1
                col += 2
            if col >= n:
                col -= 1
                row += 2
            if row < 0:
                row = 0
            if col < 0:
                col = 0
        
        return result


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
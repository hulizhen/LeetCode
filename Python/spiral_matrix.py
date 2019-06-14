class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        steps = [n, m - 1]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = 0
        row = 0
        col = -1
        result = []
        while steps[dir%2] > 0:
            for _ in range(steps[dir%2]):
                row += dirs[dir][0]
                col += dirs[dir][1]
                result.append(matrix[row][col])

            steps[dir%2] -= 1
            dir = (dir + 1) % 4
            
        return result



class Solution1(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        result = []
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Move right
            for i in range(colBegin, colEnd + 1):
                result.append(matrix[rowBegin][i])
            rowBegin += 1

            # Move down
            for i in range(rowBegin, rowEnd + 1):
                result.append(matrix[i][colEnd])
            colEnd -= 1

            # Move left
            if rowBegin <= rowEnd:
                for i in reversed(range(colBegin, colEnd + 1)):
                    result.append(matrix[rowEnd][i])
                rowEnd -= 1

            # Move up
            if colBegin <= colEnd:
                for i in reversed(range(rowBegin, rowEnd + 1)):
                    result.append(matrix[i][colBegin])
                colBegin += 1

        return result

    
print(Solution().spiralOrder([[2,5,8],[4,0,-1]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([]))
print(Solution().spiralOrder([[]]))
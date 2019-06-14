class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            nums = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    nums.append(1)
                else:
                    nums.append(result[i - 1][j - 1] + result[i - 1][j])

            result.append(nums)

        return result


print(Solution().generate(10))
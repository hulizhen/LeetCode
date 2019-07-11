class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffMap = {}
        for i, num in enumerate(numbers):
            if target - num in diffMap:
                return [diffMap[target - num] + 1, i + 1]
            else:
                diffMap[num] = i
        return []


print(Solution().twoSum([1, 2, 4, 8, 10], 12))
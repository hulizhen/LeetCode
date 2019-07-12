class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum < target:
                low += 1
            elif sum > target:
                high -= 1
            else:
                return [low + 1, high + 1]
        return []


class Solution1(object):
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


print(Solution().twoSum([1, 2, 4, 8, 16], 12))
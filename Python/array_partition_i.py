class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


class Solution1(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for (i, num) in enumerate(nums):
            if i % 2 == 0:
                result += num
        return result


print(Solution().arrayPairSum([3, 2, 4, 5, 8, 9, 1, 0, 2, 11]))

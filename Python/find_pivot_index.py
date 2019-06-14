class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = sum(nums)

        leftSum = 0
        for i, num in enumerate(nums):
            leftSum += num
            rightSum = totalSum - leftSum + num
            if leftSum == rightSum:
                return i

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))

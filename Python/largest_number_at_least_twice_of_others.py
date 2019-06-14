class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return -1

        largest = nums[0]
        largest_index = 0
        for i, num in enumerate(nums):
            if num > largest:
                largest_index = i
                largest = num

        print(largest)
        for i, num in enumerate(nums):
            if 2 * num > largest and num != largest:
                return -1

        return largest_index


print(Solution().dominantIndex([3, 6, 1, 0]))

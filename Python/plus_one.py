class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        for i in reversed(range(len(digits))):
            digits[i] += 1 if carry else 0
            carry = digits[i] / 10 >= 1
            digits[i] %= 10

        return [1] + digits if carry else digits


print(Solution().plusOne([1, 2, 3, 9]))
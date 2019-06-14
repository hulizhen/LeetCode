class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = len(a) - len(b)
        if diff > 0:
            b = '0'*diff + b
        else:
            a = '0'*-diff + a
        
        length = len(a)
        i = length - 1
        carry = False
        result = ""
        while i >= 0:
            if a[i] == '1' and b[i] == '1':
                result = ('1' if carry else '0') + result
                carry = True
            elif a[i] == '0' and b[i] == '0':
                result = ('1' if carry else '0') + result
                carry = False
            else:
                result = ('0' if carry else '1') + result
            i -= 1

        if carry:
            result = '1' + result
        return result


class Solution1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'


print(Solution().addBinary('1010101', '10101110011'))
print(Solution1().addBinary('1010101', '10101110011'))

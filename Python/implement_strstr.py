class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystackLen = len(haystack)
        needleLen = len(needle)
        if needleLen == 0:
            return 0
        if needleLen > haystackLen:
            return -1

        for i in range(haystackLen - needleLen + 1):
            for j in range(needleLen):
                if haystack[i + j] == needle[j]:
                    if j == needleLen - 1:
                        return i
                else:
                    break
        
        return -1


print(Solution().strStr("a", "a"))
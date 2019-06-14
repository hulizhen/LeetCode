class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for str in strs:
                if str[i] != c:
                    return shortest[:i]

        return shortest


class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        i = 0
        while len(strs) >= i:
            current = ""
            for j in range(len(strs)):
                if len(strs[j]) > i:
                    if len(current) == 0:
                        current = strs[j][i]
                    if strs[j][i] != current:
                        return result
                else:
                    return result
            
            result += current
            i += 1

        return result


print(Solution().longestCommonPrefix(["abc", "ab", "ab"]))
print(Solution().longestCommonPrefix([]))
print(Solution().longestCommonPrefix(["abca","abc"]))
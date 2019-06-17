class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        
        length = len(s)
        low = 0
        high = length - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1


s = ["h","e","l","l","o"]
print(s)
Solution().reverseString(s)
print(s)
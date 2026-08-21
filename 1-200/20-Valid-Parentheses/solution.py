class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d, stack = {')': '(', '}': '{', ']': '['}, []
        for c in s:
            if c in d:
                if not stack or stack.pop() != d[c]: 
                    return False
            else: 
                stack.append(c)
        return not stack

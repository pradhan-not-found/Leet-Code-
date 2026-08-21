class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans, stack = [0] * len(temperatures), []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                p = stack.pop()
                ans[p] = i - p
            stack.append(i)
        return ans

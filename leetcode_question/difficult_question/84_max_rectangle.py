class Solution:
    def largestRectangleArea(self, heights) -> int:
        res = 0
        heights = [0] + heights + [0]
        stack = [0]
        size = len(heights)

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                res = max(res, curr_width * curr_height)
            stack.append(i)

        return res


a = Solution()
a.largestRectangleArea([2,1,5,6,2,3])

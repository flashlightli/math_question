"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

 

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def restoreIpAddresses(self, s: str):
        def valid(segment):
            """
            Check if the current segment is valid :
            1. less or equal to 255
            2. the first character could be '0'
               only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            """
            Append the current list of segments
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot

        n = len(s)
        output, segments = [], []
        backtrack()

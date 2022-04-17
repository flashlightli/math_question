class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        if not k:
            return 0
        max_value, max_list = 0, []
        for i in range(1, k+1):
            if i > len(nums1) or (k-i) > len(nums2):
                continue
            nums1_index, nums2_index = i, k - i
            tmp1, tmp2 = self.get_nums(nums1, nums1_index), self.get_nums(nums2, nums2_index)
            print(tmp1, tmp2, nums1_index, nums2_index)
            tmp_result = self.merge(tmp1, tmp2)
            if max_value <= int("".join([str(i) for i in tmp_result])):
                max_value, max_list = int("".join([str(i) for i in tmp_result])), tmp_result

        print(max_list)
        return max_list

    def get_nums(self, nums, k):
        result, index = [], 0
        if not k:
            return result

        drop = len(nums) - k
        for i in nums:
            while drop and result and result[-1] < i:
                result.pop()
                drop -= 1
            result.append(i)

        return result[:k]

    def merge(self, nums1, nums2):
        result = []
        while nums1 and nums2:
            bigger = nums1 if nums1 > nums2 else nums2
            result.append(bigger[0])
            bigger.pop(0)

        return result + nums1 + nums2


a = Solution()
a.maxNumber(
    [2, 5, 6, 4, 4, 0],
    [7, 3, 8, 0, 6, 5, 7, 6, 2],
15)

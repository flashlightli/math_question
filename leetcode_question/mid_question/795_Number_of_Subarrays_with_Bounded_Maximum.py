class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        total, last_location, little_count = 0, 0, 0
        for index in range(len(nums)):
            if nums[index] > right:
                total += self.get_total_nums(nums, little_count, last_location, index)
                print("total {}".format(total))
                last_location = index + 1
                little_count = 0
            elif nums[index] < left:
                little_count += 1
            else:
                pass

        total += self.get_total_nums(nums, little_count, last_location, len(nums) - 1)

        return total

    def get_total_nums(self, nums, little_count, last_location, index):
        if index <= last_location:
            return 0

        return sum(range(index - last_location + 1))


a = Solution()
a.numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52],
32,
69)
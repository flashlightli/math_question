class Solution:
    def longestMountain(self, arr):
        if len(arr) < 3:
            return 0

        result = [1]
        max_len = 0
        curr_status = "flat"
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if curr_status == "up":
                    curr_status = "up"
                    result[i] = result[i-1] + 1
                elif curr_status == "down":
                    curr_status = "up"
                    result[i] = 1
                elif curr_status == "flat":
                    curr_status = "up"
                    result[i] = result[i - 1] + 1
            elif arr[i] < arr[i-1]:
                if curr_status == "up":
                    result[i] = result[i - 1] + 1
                    max_len = max(max_len, result[i])
                    curr_status = "down"
                elif curr_status == "flat":
                    result[i] = 1
                    curr_status = "flat"
                elif curr_status == "down":
                    result[i] = result[i - 1] + 1
                    max_len = max(max_len, result[i])
                    curr_status = "down"
            else:
                curr_status = "flat"
                result[i] = 1
                continue

        return max_len
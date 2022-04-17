class Solution:
    def smallestChair(self, times, targetFriend: int):
        if not times:
            return
        return self.handle(times, targetFriend)

    def handle(self, times, target):
        stack = [0]
        temp_dict = {0: 0}
        for index, value in enumerate(times):
            if index == 0:
                continue

            temp = []
            arrival, leave = value
            if index == 4:
                print("===")
            while stack:
                temp_index = stack.pop()
                temp_arrival, temp_leave = times[temp_index]
                if leave < temp_arrival:
                    temp_dict[index] = temp_dict.get(temp_index)
                    temp_dict[temp_index] = temp_dict.get(temp_index) + 1
                    temp += [index, temp_index]
                elif arrival < temp_arrival <= leave:
                    temp_dict[index] = temp_dict.get(temp_index)
                    temp_dict[temp_index] = temp_dict.get(temp_index) + 1
                    temp += [index, temp_index]
                elif temp_arrival < arrival <= temp_leave:
                    temp_dict[index] = temp_dict.get(temp_index) + 1
                    temp += [temp_index, index]
                elif arrival > temp_leave:
                    temp_dict[index] = temp_dict.get(temp_index)
                    temp += [temp_index, index]
                    break
            stack = stack +
            print(times)
            print(stack)
            print(temp_dict)
        return temp_dict.get(target)

# ,[52992,84310],[78492,88209]
a = Solution()
a.smallestChair(
[[33889,98676],[80071,89737],[44118,52565]]
,2
)
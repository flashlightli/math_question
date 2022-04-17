class Solution:
    def maxAliveYear(self, birth, death):
        years_total = [0] * 102
        for index in range(len(birth)):
            years_total[birth[index]-1900] += 1
            years_total[death[index]-1899] -= 1

        max_year, max_total = 1900, 0
        curr_alive = 0
        for index in range(101):
            curr_alive += years_total[index]
            if curr_alive > max_total:
                max_year = 1900 + index
                max_total = curr_alive

        print(max_year)
        return max_year

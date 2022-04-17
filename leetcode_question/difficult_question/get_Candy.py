class Solution:
    def candy(self, ratings) -> int:
        ratings_len = len(ratings)
        left, right = [], 0
        total = 0
        for i in range(ratings_len):
            if i > 0 and ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        for i in range(ratings_len- 1, -1, -1):
            if i < ratings_len - 1 and ratings[i] > ratings[i+1]:
                right += 1
            else:
                right = 1
            total = max(left[i], right)

        return total

    def candy2(self, ratings):
        n = len(ratings)
        inc, desc, pre = 1, 0 ,1
        ret = 1
        for i in range(1, n):
            if ratings[i] >= ratings[i-1]:
                desc = 0
                pre = 1 if ratings[i] == ratings[i-1] else (pre + 1)
                ret += pre
                inc = pre
            else:
                desc += 1
                if desc == inc:
                    desc += 1
                ret += desc
                pre = 1

        return ret


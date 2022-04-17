class Solution:
    def minimumBuckets(self, street: str) -> int:
        new_street = "H" + street + "H"
        street_list = new_street.split("HHH")
        if len(street_list) > 1:
            return -1

        street_list = street.split("H.H")
        bucks_count = len(street_list) - 1
        for i in "".join(street_list):
            if i == "H":
                bucks_count += 1

        return bucks_count


a = Solution()
print(a.minimumBuckets("H..H"))

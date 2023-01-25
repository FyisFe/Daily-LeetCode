# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         ans = 0

#         def incHelper(idx, cur, cnt):
#             if idx >= len(rating):
#                 return

#             nonlocal ans
#             if rating[idx] > cur:
#                 if cnt == 2:
#                     ans += 1
#                 incHelper(idx + 1, rating[idx], cnt + 1)

#             incHelper(idx + 1, cur, cnt)

#         def decHelper(idx, cur, cnt):
#             if idx >= len(rating):
#                 return

#             nonlocal ans
#             if rating[idx] < cur:
#                 if cnt == 2:
#                     ans += 1
#                 decHelper(idx + 1, rating[idx], cnt + 1)

#             decHelper(idx + 1, cur, cnt)

#         incHelper(0, 0, 0)
#         decHelper(0, 10000000, 0)
#         return ans


class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        upper_dps = [0 for _ in range(len(ratings))]
        lower_dps = [0 for _ in range(len(ratings))]

        count = 0
        for i in range(len(ratings)):
            for j in range(i):
                if ratings[j] < ratings[i]:
                    count += upper_dps[j]
                    upper_dps[i] += 1
                else:
                    count += lower_dps[j]
                    lower_dps[i] += 1

        return count

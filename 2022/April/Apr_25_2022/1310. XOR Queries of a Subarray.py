class Solution:
    def xorQueries(self, arr, queries):
        prefix_sum = [arr[0]]

        for i in range(1, len(arr)):
            prefix_sum.append(prefix_sum[i - 1] ^ arr[i])

        ans = []
        for q in queries:
            if q[0] - 1 >= 0:
                ans.append(prefix_sum[q[0] - 1] ^ prefix_sum[q[1]])
            else:
                ans.append(prefix_sum[q[1]])

        return ans

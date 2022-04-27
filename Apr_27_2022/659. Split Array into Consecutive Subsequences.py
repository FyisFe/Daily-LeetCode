from collections import Counter, defaultdict


class Solution(object):
    def isPossible(self, nums):

        freq_counter = Counter(nums)
        subseq_dict = defaultdict(int)

        for i in nums:
            if freq_counter[i] == 0:
                continue
            if subseq_dict[i - 1] > 0:
                subseq_dict[i - 1] -= 1
                subseq_dict[i] += 1
                freq_counter[i] -= 1
            elif (
                freq_counter[i] > 0
                and freq_counter[i + 1] > 0
                and freq_counter[i + 2] > 0
            ):
                freq_counter[i] -= 1
                freq_counter[i + 1] -= 1
                freq_counter[i + 2] -= 1
                subseq_dict[i + 2] += 1
            else:
                return False
        return True


sol = Solution()
sol.isPossible([1, 2, 3, 3, 4, 4, 5, 5])

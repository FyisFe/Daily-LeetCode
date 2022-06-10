class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, count, s_len = 0, 0, 0, len(s)
        hm = {}

        while end < s_len:
            if s[end] not in hm:
                hm[s[end]] = end
                end += 1

            else:
                count = max(count, end - start)
                start = hm[s[end]] + 1
                for key in hm.copy():
                    if hm[key] < start:
                        hm.pop(key)

        return max(count, end - start)

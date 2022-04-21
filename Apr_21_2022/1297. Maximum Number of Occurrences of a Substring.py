class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        idx = 0
        hm = {}

        while idx + minSize <= len(s):
            cur = s[idx : idx + minSize]
            s_set = set(cur)
            if len(s_set) > maxLetters:
                idx += 1
                continue
            if cur in hm:
                hm[cur] += 1
            else:
                hm[cur] = 1
            idx += 1
        if len(hm):
            return max(hm.values())
        return 0

        # Still TLE
        # idx = 0
        # ans = 0

        # def occurrences(string, sub):
        #     count = start = 0
        #     while True:
        #         start = string.find(sub, start) + 1
        #         if start > 0:
        #             count += 1
        #         else:
        #             return count

        # while idx + minSize < len(s):
        #     cur = s[idx : idx + minSize]
        #     s_set = set()
        #     for str in cur:
        #         s_set.add(str)
        #     if len(s_set) > maxLetters:
        #         idx += 1
        #         continue
        #     ans = max(ans, occurrences(s, cur))
        #     idx += 1
        # return ans

        # TLE
        # left = 0
        # ans = 0

        # def occurrences(string, sub):
        #     count = start = 0
        #     while True:
        #         start = string.find(sub, start) + 1
        #         if start > 0:
        #             count += 1
        #         else:
        #             return count

        # for right in range(len(s)):
        #     if right - left + 1 < minSize:
        #         continue

        #     while right - left + 1 <= maxSize and right - left + 1 >= minSize:
        #         cur = s[left : right + 1]
        #         s_set = set()
        #         for str in cur:
        #             s_set.add(str)
        #         if len(s_set) > maxLetters:
        #             left += 1
        #             break
        #         ans = max(ans, occurrences(s, cur))
        #         left += 1

        # return ans


sol = Solution()
sol.maxFreq("aaaa", 1, 3, 3)

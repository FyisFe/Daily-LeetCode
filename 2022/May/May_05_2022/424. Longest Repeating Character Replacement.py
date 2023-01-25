class Solution:
    # getting most frequent character count
    def getMFCC(self, count):
        l = 0
        for c in count:
            if count[c] > l:
                l = count[c]
        return l

    def characterReplacement(self, s: str, k: int) -> int:
        count, res, l, i = {}, 0, 0, 0
        while i < len(s):
            c = s[i]
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
            # window size update
            ws = i - l + 1
            mfcc = self.getMFCC(count)
            if ws - mfcc <= k:
                if ws > res:
                    res = ws
            else:
                count[s[l]] -= 1
                l += 1
            i += 1
        return res

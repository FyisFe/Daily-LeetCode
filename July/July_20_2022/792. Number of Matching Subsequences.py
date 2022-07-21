from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        start_idx = defaultdict(lambda: -1)
        hash_arr = [0] * n
        hash_arr[n - 1] = [-1] * 26

        for i in range(n - 2, -1, -1):
            hash_arr[i] = hash_arr[i + 1][:]
            next_char_idx = ord(s[i + 1]) - ord("a")
            hash_arr[i][next_char_idx] = i + 1
            start_idx[s[i]] = i

        res = 0
        for word in words:
            curr_idx = start_idx[word[0]]
            if curr_idx == -1:
                continue
            i = 1
            while i < len(word):
                char_idx = ord(word[i]) - ord("a")
                curr_idx = hash_arr[curr_idx][char_idx]
                if curr_idx == -1:
                    break
                i += 1
            res += 1 if i == len(word) else 0

        return res

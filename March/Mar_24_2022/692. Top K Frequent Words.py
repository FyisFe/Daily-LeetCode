class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = {}

        for word in words:
            if word in hm:
                hm[word] += 1
            else:
                hm[word] = 1

        sorted_hm = sorted(hm.items(), key=lambda x: (-x[1], x[0]))

        ans = [sorted_hm[i][0] for i in range(k)]

        return ans

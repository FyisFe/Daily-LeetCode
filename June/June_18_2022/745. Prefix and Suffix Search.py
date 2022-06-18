class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix = defaultdict(set)
        self.suffix = defaultdict(set)
        for i in range(len(words)):
            for j in range(len(words[i])):
                l = len(words[i])
                self.prefix[words[i][0 : j + 1]].add(i)
                self.suffix[words[i][l - j - 1 : l]].add(i)

    @lru_cache(maxsize=None)
    def f(self, prefix: str, suffix: str) -> int:
        res = self.prefix[prefix] & self.suffix[suffix]
        if res:
            return max(res)
        return -1

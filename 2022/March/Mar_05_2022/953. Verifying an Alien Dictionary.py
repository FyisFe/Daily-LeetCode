class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if order.find(word1[i]) < order.find(word2[i]):
                    return -1
                elif order.find(word1[i]) > order.find(word2[i]):
                    return 1
            if len(word1) < len(word2):
                return -1
            elif len(word1) > len(word2):
                return 1
            else:
                return 0

        return words == sorted(words, key=cmp_to_key(compare))

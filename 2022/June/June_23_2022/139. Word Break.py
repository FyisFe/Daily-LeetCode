from functools import lru_cache


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        while word:
            firstLetter = word[0]
            word = word[1:]
            if firstLetter not in cur.children:
                cur.children[firstLetter] = TrieNode()
            cur = cur.children[firstLetter]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        while word:
            firstLetter = word[0]
            word = word[1:]
            if firstLetter not in cur.children:
                return False
            cur = cur.children[firstLetter]
        return cur.isEnd


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        @lru_cache
        def helper(remainWord):
            if not remainWord:
                return True
            for i in range(len(remainWord)):
                if trie.search(remainWord[: i + 1]):
                    if i + 1 == len(remainWord) or helper(remainWord[i + 1 :]):
                        return True
            return False

        return helper(s)


sol = Solution()
sol.wordBreak("leetcode", ["leet", "code"])

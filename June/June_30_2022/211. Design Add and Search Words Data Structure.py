class TrieNode:
    def __init__(self) -> None:
        self.isEnd = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        while word:
            firstLetter = word[0]
            word = word[1:]
            if firstLetter not in cur.children:
                cur.children[firstLetter] = TrieNode()
            cur = cur.children[firstLetter]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def helper(cur_word: str, cur: TrieNode):
            if not cur_word:
                return cur.isEnd
            firstLetter = cur_word[0]
            if firstLetter != ".":
                if firstLetter not in cur.children:
                    return False
                return helper(cur_word[1:], cur.children[firstLetter])
            for key in cur.children:
                if helper(cur_word[1:], cur.children[key]):
                    return True
            return False

        return helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

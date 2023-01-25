class TrieNode:
    def __init__(self):
        self.children = {}  # hashmap <key: letter, value: TrieNode>
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        while word:
            firstLetter = word[0]
            word = word[1:]
            if firstLetter not in cur.children:
                cur.children[firstLetter] = TrieNode()
            cur = cur.children[firstLetter]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        while word:
            firstLetter = word[0]
            word = word[1:]
            if firstLetter not in cur.children:
                return False
            cur = cur.children[firstLetter]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        while prefix:
            firstLetter = prefix[0]
            prefix = prefix[1:]
            if firstLetter not in cur.children:
                return False
            cur = cur.children[firstLetter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

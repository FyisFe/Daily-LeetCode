class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.words = []


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def _getIndex(self, ch):
        return ord(ch) - ord("a")

    def insert(self, word):
        cur_node = self.root
        for ch in word:
            index = self._getIndex(ch)
            if cur_node.children[index] is None:
                cur_node.children[index] = TreeNode()
            cur_node = cur_node.children[index]
            cur_node.words.append(word)
        return

    def search(self, word):
        cur_node = self.root
        for ch in word:
            index = self._getIndex(ch)
            if cur_node.children[index] is None:
                return False
            cur_node = cur_node.children[index]
        return cur_node.words


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        root = Trie()
        for word in products:
            root.insert(word)
        res = []
        for i in range(len(searchWord)):
            tmp = root.search(searchWord[: i + 1])
            if tmp:
                res.append(sorted(tmp)[:3])
            else:
                res.append([])
        return res

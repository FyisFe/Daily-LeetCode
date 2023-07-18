class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        # return the value, remove from list, then add to front
        node = self.hm[key]
        self.removeNode(node)
        self.addToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.removeNode(self.hm[key])

        node = Node(key, value)
        self.hm[key] = node
        self.addToFront(node)

        if len(self.hm) > self.capacity:
            node = self.tail.prev
            self.removeNode(node)
            del self.hm[node.key]

    def addToFront(self, node: Node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

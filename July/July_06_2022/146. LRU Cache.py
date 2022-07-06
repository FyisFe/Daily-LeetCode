class DLinkListNode:
    def __init__(self):
        self.prev = None
        self.next = None
        self.val = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLinkListNode()
        self.tail = DLinkListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.capacity = capacity
        self.hm = {}

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
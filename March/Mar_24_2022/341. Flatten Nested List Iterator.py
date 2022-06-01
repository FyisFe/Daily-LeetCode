class NestedIterator(object):
    def __init__(self, nestedList):
        self.queue = collections.deque()
        for i in range(len(nestedList)):
            self.queue.append(nestedList[i])

    def next(self):
        cur = self.queue.popleft()
        return cur.getInteger()

    def hasNext(self):
        while self.queue:
            cur = self.queue[0]
            if cur.isInteger():
                return True
            self.queue.popleft()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.queue.appendleft(cur.getList()[i])
        return False

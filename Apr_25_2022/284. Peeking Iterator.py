class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_elem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked_elem is None:
            self.peeked_elem = self.iterator.next()
        return self.peeked_elem

    def next(self):
        """
        :rtype: int
        """
        elem = self.iterator.next() if self.peeked_elem is None else self.peeked_elem

        self.peeked_elem = None
        return elem

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked_elem is not None or self.iterator.hasNext()

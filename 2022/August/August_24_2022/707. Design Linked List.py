from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            self.head = ListNode(val, self.head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            cur = self.head
            for i in range(self.length - 1):
                cur = cur.next
            cur.next = ListNode(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for i in range(index - 1):
            cur = cur.next
        cur.next = ListNode(val, cur.next)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        cur = self.head

        for i in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next
        self.length -= 1

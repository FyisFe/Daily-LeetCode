class MyHashSet:
    def __init__(self):
        self.h = [0] * 1000001

    def add(self, key: int) -> None:
        self.h[key] = 1

    def remove(self, key: int) -> None:
        self.h[key] = 0

    def contains(self, key: int) -> bool:
        return self.h[key]

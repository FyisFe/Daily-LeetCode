class Solution:
    def isHappy(self, n: int) -> bool:
        prev = {n}

        while True:
            if n == 1:
                return True

            n = sum([int(c) ** 2 for c in str(n)])

            if n in prev:
                return False

            prev.add(n)

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p % 2 == 1 and q % 2 == 0:
            return 0
        if p % 2 == 1 and q % 2 == 1:
            return 1
        if p % 2 == 0 and q % 2 == 1:
            return 2
        if p % 2 == 0 and q % 2 == 0:
            return self.mirrorReflection(p / 2, q / 2)

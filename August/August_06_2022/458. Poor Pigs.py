class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        round = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, round + 1))

class Solution:
    def deleteAndEarn(self, nums) -> int:
        earn_val = defaultdict(int)
        mem = {}
        max_num = 0

        for num in nums:
            earn_val[num] += num
            max_num = max(max_num, num)

        def helper(num):
            if num == 0:
                return 0

            if num == 1:
                return earn_val[1]

            if num in mem:
                return mem[num]

            mem[num] = max(helper(num - 1), earn_val[num] + helper(num - 2))
            return mem[num]

        return helper(max_num)

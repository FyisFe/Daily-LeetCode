class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(cur):
            if not len(cur):
                return 0
            if cur[0] == "(" and cur[1] == ")":
                return 1 + helper(cur[2:])

            stack = ["("]
            idx = 1

            while len(stack):
                if cur[idx] == "(":
                    stack.append("(")
                else:
                    stack.pop()
                idx += 1

            return 2 * helper(cur[1 : idx - 1]) + helper(cur[idx:])

        return helper(s)

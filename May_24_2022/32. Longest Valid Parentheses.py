class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        cur_length = 0
        ans = 0
        for e in s:
            if e == ")":
                if stack:
                    cur_length += stack.pop() + 2
                    ans = max(ans, cur_length)
                else:
                    cur_length = 0
            elif e == "(":
                stack.append(cur_length)
                cur_length = 0
        return ans

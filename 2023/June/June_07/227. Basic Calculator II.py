class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        if s == "0":
            return 0
        num, sign, stack = 0, "+", []
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord("0")
            if (not ch.isdigit() and ch != " ") or i == n - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = ch
                num = 0
        return sum(stack)

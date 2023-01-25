class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                op1, op2 = stack.pop(-1), stack.pop(-1)
                res = None
                if token == "+":
                    res = op1 + op2
                elif token == "-":
                    res = op2 - op1
                elif token == "*":
                    res = op1 * op2
                else:
                    res = int(op2 / op1)
                stack.append(res)
        return stack.pop(-1)

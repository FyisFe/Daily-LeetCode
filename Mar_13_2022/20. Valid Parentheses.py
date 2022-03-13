class Solution:
    def isValid(self, s: str) -> bool:
        que = []

        for chr in s:
            if chr == "(" or chr == "[" or chr == "{":
                que.append(chr)
            else:
                if len(que) == 0:
                    return False
                top = que.pop()
                if not (
                    (top == "(" and chr == ")")
                    or (top == "[" and chr == "]")
                    or (top == "{" and chr == "}")
                ):
                    return False
        if len(que):
            return False
        return True

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split("/"):
            if p == ".." and len(stack):
                stack.pop()
            elif p == "" or p == "." or p == "..":
                continue
            else:
                stack.append(p)

        return "/" + "/".join(stack)

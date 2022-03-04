class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        idx = 0
        while idx < len(command):
            if command[idx] == "G":
                res += "G"
                idx += 1
            elif command[idx] == "(" and command[idx + 1] == ")":
                res += "o"
                idx += 2
            else:
                res += "al"
                idx += 4
        return res

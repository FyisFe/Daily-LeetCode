class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                # pop until '['
                pattern = ""
                while stack and stack[-1] != "[":
                    pattern = stack.pop() + pattern
                stack.pop()
                # get repeat times
                time = ""
                while stack and stack[-1].isdigit():
                    time = stack.pop() + time

                repeat_pattern = int(time) * pattern

                # push repeat_pattern back to stack
                for i in range(len(repeat_pattern)):
                    stack.append(repeat_pattern[i])

        # construct output
        return "".join(stack)

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            return f'{s[0].lower()}*****{s[s.index("@")-1].lower()+"".join([x.lower() for x in s[s.index("@"):]])}'
        s = "".join([x for x in s if x not in "()- +"])
        return (
            "" if len(s) <= 10 else "+" + "*" * (len(s) - 10) + "-"
        ) + f"***-***-{s[-4:]}"

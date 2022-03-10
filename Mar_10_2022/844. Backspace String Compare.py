class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Reverse the string, then you can access the # at first, means you can know if the following characters are deleted or not

        O(n) time and O(1) Space
        """

        def generater(S):
            skip = 0
            for x in S:
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(
            x == y for x, y in itertools.izip_longest(generater(s), generater(t))
        )
        """
        Generate Actual String then Compare them
        O(N) time and O(N) space

        def getActualStr(source):
              res = ""
              for chr in source:
                  if chr == "#":
                      if res == "":
                          continue
                      res = res[:-1]
                  else:
                      res += chr
              return res

          return getActualStr(s) == getActualStr(t)
        """

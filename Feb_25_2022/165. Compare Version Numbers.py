class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")

        l1, l2 = len(v1), len(v2)

        i = j = 0

        while i < l1 or j < l2:
            intV1 = int(v1[i]) if i < l1 else 0
            intV2 = int(v2[j]) if j < l2 else 0

            if intV1 < intV2:
                return -1

            if intV1 > intV2:
                return 1

            i, j = i + 1, j + 1

        return 0

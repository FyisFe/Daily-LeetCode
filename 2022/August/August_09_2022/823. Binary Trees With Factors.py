class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s = set(arr)
        mp = {}
        ans = 0
        # To minimize the traversal time
        arr.sort()

        def f(el):
            a = 1
            if el in mp:
                return mp[el]
            for x in arr:
                if x > math.sqrt(el):
                    break
                if el / x in s:
                    if el / x == x:
                        a += f(int(el / x)) * f(x)
                    else:
                        a += f(int(el / x)) * f(x) * 2
            mp[el] = a
            return a

        for i in range(len(arr)):
            ans += f(arr[i])
        return (ans) % (pow(10, 9) + 7)

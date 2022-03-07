class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def compare(num1, num2):
            sum1 = sum(int(digit) for digit in str(format(num1, "b")))
            sum2 = sum(int(digit) for digit in str(format(num2, "b")))

            if sum1 == sum2:
                return num1 - num2
            return sum1 - sum2

        return sorted(arr, key=cmp_to_key(compare))

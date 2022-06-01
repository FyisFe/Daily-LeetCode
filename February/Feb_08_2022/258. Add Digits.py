def addDigits(num: int) -> int:
    if num < 10:
        return num
    else:
        return addDigits(sum([int(x) for x in str(num)]))

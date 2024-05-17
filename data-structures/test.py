def test(count=None):
    n = 7
    while n > 0:
        # print(n << i, end="")
        if n & 1:
            count += 1
        n >>= 1
        # print(n << i, end="")
    return count


print(test(0))

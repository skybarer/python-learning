a = 5  # binary: 0101
b = 3  # binary: 0011

print(bin(a)[2:])
print(bin(b)[2:])
print(a & b)  # binary: 0001, which is 1 in decimal
print(a | b)  # binary: 0111, which is 7 in decimal
print(a ^ b)  # binary: 0110, which is 6 in decimal
print(~a)  # binary: 1010 (2's complement representation), which is -6 in decimal
print(a << 1)  # binary: 1010, which is 10 in decimal
print(a >> 1)  # binary: 0010, which is 2 in decimal


# 1. Checking if a Number is a Power of Two
# 2. Counting the Number of Set Bits (Hamming Weight) python
# 3. Finding the Only Non-Repeating Element
# 4. Swapping Two Numbers Without a Temporary Variable
# 5. Finding the Two Unique Numbers in an Array
# 6. Finding the Missing Number in an Array
# 8. Generating All Subsets (Power Set)
# 9. Finding Maximum XOR of Two Numbers in an Array
# 10. Checking if a Number Has Alternating Bits
# 11. Finding the Next Power of 2
# 12. Finding the Longest Consecutive Sequence of 1s in Binary Representation
# 13. Reversing Bits of a Number
# 14. Number of Bits to Change to Convert A to B
# 15. Divide Two Integers Without Using Division


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


# Example usage
print(is_power_of_two(4))  # True
print(is_power_of_two(5))  # False


def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


# Example usage
print(count_set_bits(5))  # 2 (binary: 101)


def find_single_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


# Example usage
arr = [4, 1, 2, 1, 2]
print(find_single_element(arr))  # 4


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# Example usage
a, b = 3, 4
a, b = swap(a, b)
print(a, b)  # 4, 3


def find_two_unique_elements(arr):
    xor_sum = 0
    for num in arr:
        xor_sum ^= num

    # Find a set bit (there must be at least one set bit in xor_sum)
    set_bit = xor_sum & -xor_sum

    # Divide elements into two groups and XOR separately
    unique1 = unique2 = 0
    for num in arr:
        if num & set_bit:
            unique1 ^= num
        else:
            unique2 ^= num

    return unique1, unique2


# Example usage
arr = [1, 2, 1, 3, 2, 5]
print(find_two_unique_elements(arr))  # (3, 5)


def find_missing_number(arr):
    n = len(arr)
    total_xor = 0
    arr_xor = 0

    for i in range(n + 1):
        total_xor ^= i

    for num in arr:
        arr_xor ^= num

    return total_xor ^ arr_xor


# Example usage
arr = [3, 0, 1]
print(find_missing_number(arr))  # 2


def generate_subsets(arr):
    n = len(arr)
    subsets = []

    for i in range(1 << n):  # 2^n possible subsets
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        subsets.append(subset)

    return subsets


# Example usage
arr = [1, 2, 3]
print(generate_subsets(arr))


# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def find_maximum_xor(arr):
    max_xor = 0
    mask = 0

    for i in range(31, -1, -1):
        mask |= (1 << i)
        found_prefixes = {num & mask for num in arr}

        temp_max_xor = max_xor | (1 << i)

        for prefix in found_prefixes:
            if (prefix ^ temp_max_xor) in found_prefixes:
                max_xor = temp_max_xor
                break

    return max_xor


# Example usage
arr = [3, 10, 5, 25, 2, 8]
print(find_maximum_xor(arr))  # 28 (5 ^ 25)


def has_alternating_bits(n):
    prev_bit = n & 1
    n >>= 1

    while n:
        current_bit = n & 1
        if current_bit == prev_bit:
            return False
        prev_bit = current_bit
        n >>= 1

    return True


# Example usage
print(has_alternating_bits(5))  # True (binary: 101)
print(has_alternating_bits(7))  # False (binary: 111)


def next_power_of_2(n):
    if n == 0:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n |= n >> 32  # For 64-bit integers
    return n + 1


# Example usage
print(next_power_of_2(5))  # 8
print(next_power_of_2(17))  # 32


def reverse_bits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= (n & 1)
        n >>= 1
    return result


# Example usage
n = 43261596  # binary: 00000010100101000001111010011100
print(reverse_bits(n))  # 964176192, binary: 00111001011110000010100101000000


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero")

    if dividend == 0:
        return 0

    sign = (-1 if ((dividend < 0) ^ (divisor < 0)) else 1)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i

    return sign * quotient


# Example usage
dividend = 10
divisor = 3
print(divide(dividend, divisor))  # 3

def find_max_min(arr):
    if not arr:
        return None, None

    # Initialize max and min with the first element of the array
    max_value = arr[0]
    min_value = arr[0]

    # Iterate through the array to find the maximum and minimum values
    for num in arr:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    return max_value, min_value


# Example usage:
array = [3, 1, 4, 7, 2, 9, 5]   
max_val, min_val = find_max_min(array)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

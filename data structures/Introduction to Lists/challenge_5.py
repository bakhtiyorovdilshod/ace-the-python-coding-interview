def find_minimum(arr):
    # Write your code here
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


def find_second_maximum(lst):
    # Write your code here
    first_max, second_max = float('-inf')
    for i in range(len(lst)):
        if lst[i] > first_max:
            second_max = first_max
            first_max = lst[i]
        elif lst[i] > second_max and lst[i] != first_max:
            second_max = lst[i]
    if second_max == float('-inf'):
        return
    else:
        return second_max

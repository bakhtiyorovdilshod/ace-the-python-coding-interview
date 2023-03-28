def find_product(lst):
    # Write your code here
    all_product = 1
    for e in lst:
        all_product = all_product * e

    for ind, val in enumerate(lst):
        if val != 0:
            lst[ind] = all_product / val
        else:
            lst[ind] = all_product
    return lst

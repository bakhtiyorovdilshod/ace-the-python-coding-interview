def find_first_unique(lst):
    # Write your code here
    copy_list = lst.copy()
    for ind, val in enumerate(lst):
        copy_list.pop(ind)
        if val not in copy_list:
            return val
        else:
            copy_list.insert(ind, val)
    return False


find_first_unique([4, 5, 1, 2, 0, 4])

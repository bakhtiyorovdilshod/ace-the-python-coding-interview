def rearrange(lst):
    # Write your code here
    positive_elements = []
    negative_elements = []
    for e in lst:
        if e >= 0:
            positive_elements.append(e)
        else:
            negative_elements.append(e)
    return positive_elements + negative_elements


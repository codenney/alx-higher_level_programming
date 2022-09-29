#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = []
    for num in set_1:
        a.append(num)

    common = [x for x in a if x in set_2]

    for num in set_2:
        a.append(num)
    uniq = [x for x in a if x not in common]

    return uniq

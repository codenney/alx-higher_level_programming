#!/usr/bin/python3
def uniq_add(my_list=[]):
    dem_uniq = []
    for num in my_list:
        if num not in dem_uniq:
            dem_uniq.append(num)
    return sum(dem_uniq)

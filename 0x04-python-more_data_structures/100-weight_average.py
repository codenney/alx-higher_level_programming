#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0    
    sumAll = 0
    divideBy = 0

    for item in my_list:
        sumAll += item[0] * item[1]
        divideBy += item[1]
    return sumAll / divideBy

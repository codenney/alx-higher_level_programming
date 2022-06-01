#!/usr/bin/python3
for num in range(122, 96, -1):
    if num % 2 == 1:
        print('{:c}'.format(num - 32), end='')
    else:
        print('{:c}'.format(num), end='')

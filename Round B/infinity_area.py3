# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem A. Infinity Area
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf079
#
# Time:  O(logR)
# Space: O(1)
#

from math import pi

def infinity_area():
    R, A, B = map(int, input().split())
    result = parity = 0
    while R:
        result += R**2
        if parity == 0:
            R *= A
        else:
            R //= B
        parity ^= 1
    return pi * result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, infinity_area()))

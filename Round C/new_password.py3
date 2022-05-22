# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round C - Problem A. New Password
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15
#
# Time:  O(N)
# Space: O(1)
#

from string import ascii_lowercase, ascii_uppercase

def new_password():
    N = int(input())
    P = list(input())
    result = P[:]
    for requirement in (UPPER, LOWER, DIGIT, SPECIAL):
        if not any(x in requirement for x in P):
            result.append(next(iter(requirement)))
    result.append(next(iter(UPPER))*(7-len(result)))
    return "".join(result)

UPPER = set(ascii_uppercase)
LOWER = set(ascii_lowercase)
DIGIT = set(str(i) for i in range(10))
SPECIAL = set('#@*&')
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, new_password()))

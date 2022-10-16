# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round G - Problem B. Curling
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17c82
#
# Time:  O(N + M)
# Space: O(N + M)
#

def curling():
    R_square = sum(map(int, input().split()))**2
    stones = [[list(map(int, input().split())) for _ in range(int(input()))] for _ in range(2)]
    mn = [min((X**2+Y**2 for X, Y in stones[i]), default=float("inf")) for i in range(2)]
    result = [sum(X**2+Y**2 <= min(mn[i^1]-1, R_square) for X, Y in stones[i]) for i in range(2)]
    return "{} {}".format(*result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, curling()))

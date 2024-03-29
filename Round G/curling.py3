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
    dist_squares = [[sum(map(lambda x: int(x)**2, input().split())) for _ in range(int(input()))] for _ in range(2)]
    mn = [min(dist_squares[i], default=float("inf")) for i in range(2)]
    return "{} {}".format(*(sum(d <= min(mn[i^1]-1, R_square) for d in dist_squares[i]) for i in range(2)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, curling()))

# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round F - Problem A. Sort the Fabrics
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000beefbb
#
# Time:  O(MAX_C * NlogN), MAX_C is max(len(C) for C, _, _ in fabrics)
# Space: O(MAX_C * N)
#

def sort_the_fabrics():
    N = int(input())
    fabrics = [input().split() for _ in range(N)]
    A = sorted((C, int(U)) for C, _, U in fabrics)
    B = sorted((int(D), int(U)) for _, D, U in fabrics)
    return sum(a == b for (_, a), (_, b) in zip(A, B))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sort_the_fabrics()))

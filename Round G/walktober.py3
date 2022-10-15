# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round G - Problem A. Walktober
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c174f2
#
# Time:  O(M * N)
# Space: O(N)
#

def walktober():
    M, N, P = map(int, input().split())
    mx = [0]*N
    for p in range(M):
        scores = list(map(int, input().split()))
        for i, x in enumerate(scores):
            mx[i] = max(mx[i], x)
        if p == P-1:
            john = scores
    return sum(x-y for x, y in zip(mx, john))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, walktober()))

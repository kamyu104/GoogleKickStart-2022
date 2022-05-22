# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round C - Problem C. Ants on a Stick
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b209bc
#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import deque

def ants_on_a_stick():
    N, L = map(int, input().split())
    P, D = [0]*N, [0]*N
    for i in range(N):
        P[i], D[i] = map(int, input().split())
    result = []
    ants = deque(sorted(range(N), key=lambda x: P[x]))
    prev = -1
    for p, d in sorted((P[i], D[i]) if not D[i] else (L-P[i], D[i]) for i in range(N)):
        if not d:
            result.append(ants.popleft()+1)
        else:
            result.append(ants.pop()+1)
        if p == prev:
            if result[-2] > result[-1]:
                result[-2], result[-1] = result[-1], result[-2]
        prev = p
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ants_on_a_stick()))

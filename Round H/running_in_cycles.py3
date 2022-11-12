# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round H - Problem A. Running in Circles
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c4766e
#
# Time:  O(N)
# Space: O(1)
#

def norm(x, L):
    q, r = divmod(abs(x), L)
    return (q, r) if x >= 0 else (q, -r)

def running_in_cycles():
    L, N = map(int, input().split())
    result = curr = 0
    for _ in range(N):
        D, C = list(input().split())
        D = int(D)
        curr += D if C == 'C' else -D
        cnt, curr = norm(curr, L)
        result += cnt
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, running_in_cycles()))

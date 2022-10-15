# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round G - Problem C. Happy Subarrays
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17491
#
# Time:  O(N)
# Space: O(N)
#

def happy_subarrays():
    N = int(input())
    A = list(map(int, input().split()))
    P = [0]*(N+1)
    for i in range(N):
        P[i+1] = P[i]+A[i]
    stk = []
    result = curr = 0
    for p in P:
        while stk and stk[-1] > p:
            curr -= stk.pop()
        result += len(stk)*p-curr
        stk.append(p)
        curr += p
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, happy_subarrays()))

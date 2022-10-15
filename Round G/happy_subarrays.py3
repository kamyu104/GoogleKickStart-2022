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
    right = [-1]*(N+1)
    stk = []
    for i in reversed(range(N+1)):
        while stk and P[stk[-1]] >= P[i]:
            stk.pop()
        if i+1 < len(right):
            right[i+1] = stk[-1]-1 if stk else N
        stk.append(i)
    PP = [0]*(N+1)
    for i in range(N):
        PP[i+1] += PP[i]+P[i+1]
    return sum(PP[right[i]]-PP[i-1]-(right[i]-i+1)*P[i-1] for i in range(1, N+1))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, happy_subarrays()))

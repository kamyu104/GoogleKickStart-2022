# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem B. Maximum Gain
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae
#
# Time:  O(K^2 + N + M), pass in PyPy3 but Python3
# Space: O(N + M)
#

def max_sum(A, K):
    prefix = [0]*(len(A)+1)
    for i in range(len(A)):
        prefix[i+1] = prefix[i]+A[i]
    return [max(prefix[i]+(prefix[-1]-prefix[-1-(c-i)]) for i in range(c+1)) for c in range(min(K, len(A))+1)]

def maximum_gain():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    cnt1, cnt2 = max_sum(A, K), max_sum(B, K)
    return max(cnt1[i]+cnt2[K-i] for i in range(min(K, len(A))+1) if 0 <= K-i <= len(B))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, maximum_gain()))

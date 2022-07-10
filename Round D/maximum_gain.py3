# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem B. Maximum Gain
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae
#
# Time:  O(K * (N + M)), pass in PyPy3 but Python3
# Space: O(1)
#

def max_sum_with_count(A, cnt):
    l = len(A)-cnt
    if not l:
        return sum(A)
    result = float("inf")
    total = 0
    for i in range(len(A)):
        total += A[i]
        if i-l+1 < 0:
            continue
        result = min(result, total)
        total -= A[i-l+1]
    return sum(A)-result

def maximum_gain():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    return max(max_sum_with_count(A, i)+max_sum_with_count(B, K-i) for i in range(max(K-len(B), 0), min(K, len(A))+1))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, maximum_gain()))

# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem B. Maximum Gain
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae
#
# Time:  O(K^2 + N + M), pass in PyPy3 but Python3
# Space: O(1)
#

def min_sum_with_count(A, total, l):
    result = total
    for i in range(l, len(A)):
        total += A[i]-A[i-l]
        result = min(result, total)
    return result

def maximum_gain():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    K = len(A)+len(B)-K
    total1, total2 = sum(A[i] for i in range(max(K-len(B), 0))),  sum(B[i] for i in range(min(K, len(B))))
    result = float("inf")
    for i in range(max(K-len(B), 0), min(K, len(A))+1):
        result = min(result, min_sum_with_count(A, total1, i)+min_sum_with_count(B, total2, K-i))
        if i < len(A):
            total1 += A[i]
        if (K-i)-1 >= 0:
            total2 -= B[(K-i)-1]
    return sum(A)+sum(B)-result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, maximum_gain()))

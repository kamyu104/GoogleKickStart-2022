# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem B. Maximum Gain
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae
#
# Time:  O(K^2 + N + M), pass in PyPy3 but Python3
# Space: O(1)
#

def max_sum_with_count(A, total, curr, l):
    result = curr
    for i in range(l, len(A)):
        curr += A[i]-A[i-l]
        result = min(result, curr)
    return total-result

def maximum_gain():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    K = len(A)+len(B)-K
    total1, total2 = sum(A), sum(B)
    curr1, curr2 = sum(A[i] for i in range(max(K-len(B), 0))),  sum(B[i] for i in range(min(K, len(B))))
    result = 0
    for i in range(max(K-len(B), 0), min(K, len(A))+1):
        result = max(result, max_sum_with_count(A, total1, curr1, i)+max_sum_with_count(B, total2, curr2, K-i))
        if i < len(A):
            curr1 += A[i]
        if (K-i)-1 >= 0:
            curr2 -= B[(K-i)-1]
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, maximum_gain()))

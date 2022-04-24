# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem B. Palindromic Factors
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acee89
#
# Time:  O(sqrt(A) * log(A))
# Space: O(1)
#

def is_palindrome(x):
    y, n = 0, x
    while n:
        n, r = divmod(n, 10)
        y = y*10+r
    return x == y

def palindromic_factors():
    A = int(input())
    result = 0
    curr = 1
    while curr*curr <= A:
        if A%curr == 0:
             result += is_palindrome(curr)
             if A//curr != curr:
                 result += is_palindrome(A//curr)
        curr += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, palindromic_factors()))

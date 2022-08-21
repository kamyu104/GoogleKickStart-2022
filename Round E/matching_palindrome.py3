# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem C. Matching Palindrome
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba82c5
#
# Time:  O(N * sqrt(N))
# Space: O(1)
#

def is_palindrome(P, left, right):
    while left < right:
        if P[left] != P[right]:
            return False
        left, right = left+1, right-1
    return True

def matching_palindrome():
    N = int(input())
    P = input()
    for l in range(1, len(P)):
        if len(P)%l:
            continue
        if is_palindrome(P, 0, l-1) and is_palindrome(P, l, len(P)-1):
            return P[:l]
    return P

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, matching_palindrome()))

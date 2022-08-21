# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem C. Matching Palindrome
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba82c5
#
# Time:  O(N)
# Space: O(N)
#

def manacher(s):
    s = '^#' + '#'.join(s) + '#$'
    P = [0]*len(s)
    C, R = 0, 0
    for i in range(1, len(s)-1):
        i_mirror = 2*C-i
        if R > i:
            P[i] = min(R-i, P[i_mirror])
        while s[i+1+P[i]] == s[i-1-P[i]]:
            P[i] += 1
        if i+P[i] > R:
            C, R = i, i+P[i]
    return P

def matching_palindrome():
    N = int(input())
    P = input()
    p = manacher(P)
    l = min(p[i] for i in range(2, (len(p)-2)+1) if p[i] != 0 and p[(len(p)-2)-p[i]] == p[i] and p[1+(N-p[i])] == N-p[i])
    return P[:l]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, matching_palindrome()))

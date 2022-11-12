# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round H - Problem B. Magical Well Of Lilies
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47e79
#
# Time:  O(MAX_L * log(MAX_L))
# Space: O(MAX_L)
#

def magical_of_lilies():
    L = int(input())
    return DP[L]

MAX_L = 10**5
DP = [float("inf")]*(MAX_L+1)
DP[0] = 0
for i in range(1, MAX_L+1):
    DP[i] = min(DP[i], DP[i-1]+1)
    for j in range(2*i, MAX_L+1, i):
        DP[j] = min(DP[j], DP[i]+4+2*(j//i-1))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, magical_of_lilies()))

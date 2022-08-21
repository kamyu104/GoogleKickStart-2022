# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem B. Students and Mentors
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba84ae
#
# Time:  O(NlogN)
# Space: O(N)
#

from bisect import bisect_left

def students_and_mentors():
    N = int(input())
    R = list(map(int, input().split()))
    sorted_R = sorted((r, i) for i, r in enumerate(R))
    result = [-1]*N
    for i, r in enumerate(R):
        j = bisect_left(sorted_R, (2*r+1,))-1
        if j < 0:
            continue
        if sorted_R[j][1] != i:
            result[i] = R[sorted_R[j][1]]
        elif j-1 >= 0:
            result[i] = R[sorted_R[j-1][1]]
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, students_and_mentors()))

# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem B. Students and Mentors
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba84ae
#
# Time:  O(NlogN)
# Space: O(N)
#

def students_and_mentors():
    N = int(input())
    R = list(map(int, input().split()))
    idx = list(range(N))
    idx.sort(key=lambda x: R[x])
    result = [-1]*N
    right = 0
    for left in range(N):
        while right+1 < N and R[idx[right+1]] <= 2*R[idx[left]]:
            right += 1
        if left != right:
            result[idx[left]] = R[idx[right]]
        elif right-1 >= 0:
            result[idx[left]] = R[idx[right-1]]
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, students_and_mentors()))

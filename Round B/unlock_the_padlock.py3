# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem C. Unlock the Padlock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acef55
#
# Time:  O(N^2)
# Space: O(N^2)
#

def unlock_the_padlock():
    def memoization(left, right, x, lookup):  # use lookup instead of lru_cache which results in MLE in Python3
        if (left, right, x) not in lookup:
            l = left
            while l <= right and V[l] == V[left]:
                l += 1
            r = right
            while r >= left and V[r] == V[right]:
                r -= 1
            lookup[left, right, x] = min((memoization(l, right, V[left], lookup) if l <= right else 0) + min((V[left]-x)%D, D-(V[left]-x)%D),
                                         (memoization(left, r, V[right], lookup) if left <= r else 0) + min((V[right]-x)%D, D-(V[right]-x)%D))
        return lookup[left, right, x]

    N, D = map(int, input().split())
    V = list(map(int, input().split()))
    return memoization(0, N-1, 0, {})

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, unlock_the_padlock()))

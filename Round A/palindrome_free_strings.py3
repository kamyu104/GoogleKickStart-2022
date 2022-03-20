# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem C. Palindrome Free Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
#
# Time:  O(N)
# Space: O(N)
#

def check(s, i):
    for left, right in [(i-4, i), (i-5, i)]:
        if left < 0:
            continue
        while left < right:
            if s[left] != s[right]:
                break
            left, right = left+1, right-1
        if left >= right:
            return False
    return True

def iter_backtracking(s):  # backtrack only the valid states, of which number is O(N)
    lookup = {i for i, x in enumerate(s) if x == '?'}
    stk = []
    i = 0
    while i < len(s):
        if i in lookup:
            s[i] = '0'
            stk.append(i)
        while not check(s, i):
            if not stk:
                return False
            i = stk.pop()
            s[i] = '1'
        i += 1
    return True

def palindrome_free_strings():
    N = int(input().strip())
    S = list(input().strip())
    return "POSSIBLE" if iter_backtracking(S) else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, palindrome_free_strings()))

# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem C. Palindrome Free Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
#
# Time:  O(N)
# Space: O(N)
#

def check(s):
    return len(s) <= 4 or s != s[::-1]

def iter_backtracking(s):  # backtrack only the valid states, of which number is O(N)
    lookup = {i for i, x in enumerate(s) if x == '?'}
    stk = []
    i = 0
    while i < len(s):
        if i in lookup:
            s[i] = '0'
            stk.append(i)
        while not (check(s[i-4:i+1]) and check(s[i-5:i+1])):
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

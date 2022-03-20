# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem C. Palindrome Free Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
#
# Time:  O(N)
# Space: O(1)
#

def check(s):
    if len(s) <= 4:
        return True
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return True
        left, right = left+1, right-1
    return False

def dp(s):
    dp = {''}
    for c in s:
        dp = {y[-5:] for x in dp for y in ([x+'0', x+'1'] if c == '?' else [x+c]) if check(y[-5:]) and check(y[-6:])}
    return dp
        
def palindrome_free_strings():
    N = int(input().strip())
    S = list(input().strip())
    return "POSSIBLE" if dp(S) else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, palindrome_free_strings()))

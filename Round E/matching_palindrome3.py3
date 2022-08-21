# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem C. Matching Palindrome
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba82c5
#
# Time:  O(N)
# Space: O(N)
#

def getPrefix(pattern):
    prefix = [-1]*len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j != -1 and pattern[j+1] != pattern[i]:
            j = prefix[j]
        if pattern[j+1] == pattern[i]:
            j += 1
        prefix[i] = j
    return prefix

def matching_palindrome():
    N = int(input())
    P = input()
    PP = P+P
    prefix = getPrefix(PP)
    return PP[prefix[-1]+1:]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, matching_palindrome()))

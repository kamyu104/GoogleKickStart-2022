# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem A. Coloring Game
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba856a
#
# Time:  O(1)
# Space: O(1)
#

def ceil_divide(a, b):
    return (a+b-1)//b

def coloring_game():
    N = int(input())
    return ceil_divide(N, 5)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, coloring_game()))

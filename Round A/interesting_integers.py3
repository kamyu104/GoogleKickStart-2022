# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem D. Interesting Integers
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
#
# Time:  O(M * (9M)^3), M is max(len(digits))
# Space: O(M * (9M)^3)
#

from functools import lru_cache

@lru_cache(None)
def memoization(target, l, product, total):  # Total Time: O(M * (9M)^3)
    if l == 0:
        return int(total == target and product == 0)
    return sum(memoization(target, l-1, (product*x)%target, total+x) for x in range(10))

def count_with_number_of_digits(target, l):  # Time: O(1)
    return sum(memoization(target, l-1, x%target, x) for x in range(1, 10))

def count_with_prefix_of_digits(target, digits):  # Time: O(len(digits))
    result = 0
    product, total = 1, 0
    for i, x in enumerate(digits):
        result += sum(memoization(target, (len(digits)-1)-i, (product*x)%target, total+x) for x in range(int(i == 0), x))
        product, total = (product*x)%target, total+x
    result += memoization(target, 0, product, total)
    return result

def f(x):  # Time: O(len(digits)^2)
    digits = list(map(int, str(x)))
    result = 0
    for target in range(1, 9*len(digits)+1):
        for l in range(1, len(digits)):
            result += count_with_number_of_digits(target, l)
        result += count_with_prefix_of_digits(target, digits)
    return result

def interesting_integers():
    A, B = list(map(int, input().strip().split()))
    return f(B)-f(A-1)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, interesting_integers()))

# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem D. Palinedrome Free Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
#
# Time:  O(N)
# Space: O(N)
#

def g(l, product, total, target):
    if l == 0:
        return int(total == target and product == 0)
    if (l, product, total, target) not in lookup:
        lookup[(l, product, total, target)] = sum(g(l-1, (product*x)%target, total+x, target) for x in range(0, 9+1))
    return lookup[(l, product, total, target)]

def count_interesting_integers_with_number_of_digits(target, l):
    return sum(g(l-1, x%target, x, target) for x in range(1, 9+1))

def count_interesting_integers_with_prefix_of_digits(target, digits, product, total, i, is_first):
    if i == len(digits):
        return int(product%total == 0 and total == target)
    return sum(g((len(digits)-1)-i, (product*x)%target, total+x, target) for x in range(is_first, digits[i])) + \
           count_interesting_integers_with_prefix_of_digits(target, digits, (product*digits[i])%target, total+digits[i], i+1, 0)

def f(x):
    if x == 0:
        return 0
    digits = list(map(int, str(x)))
    count = 0
    for target in range(1, 9*len(digits)+1):
        for l in range(1, len(digits)):
            count += count_interesting_integers_with_number_of_digits(target, l)
        count += count_interesting_integers_with_prefix_of_digits(target, digits, 1, 0, 0, 1)
    return count

def interesting_integers():
    A, B = list(map(int, input().strip().split()))
    return f(B)-f(A-1)

lookup = {}
for case in range(eval(input())):
    print('Case #%d: %s' % (case+1, interesting_integers()))
# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem A. Image Labeler
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76e11
#
# Time:  O(N), pass in PyPy3 but Python3
# Space: O(1)
#

from random import seed, randint

def nth_element(nums, left, n, right, compare=lambda a, b: a < b):
    def partition_around_pivot(left, right, pivot_idx, nums, compare):
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in range(left, right):
            if compare(nums[i], nums[right]):
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

    while left <= right:
        pivot_idx = randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx, nums, compare)
        if new_pivot_idx == n:
            return
        elif new_pivot_idx > n:
            right = new_pivot_idx - 1
        else:  # new_pivot_idx < n
            left = new_pivot_idx + 1

def image_labeler():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    nth_element(A, 0, (N-(M-1))-1, N-1)
    nth_element(A, 0, (0+((N-(M-1))-1))//2, (N-(M-1))-1)
    nth_element(A, (0+((N-(M-1))-1))//2+1, (0+((N-(M-1))-1))//2+1, (N-(M-1))-1)
    return (A[(0+((N-(M-1))-1))//2] if (N-(M-1))%2 else (A[(0+((N-(M-1))-1))//2]+A[(0+((N-(M-1))-1))//2+1])/2.0) + sum(A[~i] for i in range(M-1))

seed(0)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, image_labeler()))

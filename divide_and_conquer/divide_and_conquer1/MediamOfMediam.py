import numpy as np
import random


rd = random.Random()
rd.seed(0)


def mom_select(arr, k):
    if len(arr) < 50:
        return quick_select(arr, k)
    new_arr = list(np.reshape(arr, (5, -1)).transpose())
    medium_arr = [quick_select(list(row), 3) for row in new_arr]
    pivot_num = mom_select(medium_arr, len(arr) // 10)
    left_arr, mid_arr, right_arr = three_partition_num(arr, pivot_num)
    if k <= len(left_arr):
        return mom_select(left_arr, k)
    elif k > len(left_arr) + len(mid_arr):
        return mom_select(right_arr, k - len(left_arr) - len(mid_arr))
    else:
        return pivot_num


def three_partition_num(arr, pivot_num):
    left_arr = []
    middle_arr = []
    right_arr = []
    for item in arr:
        if item < pivot_num:
            left_arr.append(item)
        elif item == pivot_num:
            middle_arr.append(item)
        else:
            right_arr.append(item)
    return left_arr, middle_arr, right_arr


def quick_select(arr, k):
    left_arr, mid_arr, right_arr = three_partition(arr)
    if k <= len(left_arr):
        return quick_select(left_arr, k)
    elif k > len(left_arr) + len(mid_arr):
        return quick_select(right_arr, k - len(left_arr) - len(mid_arr))
    else:
        return mid_arr[0]


def three_partition(arr):
    left_arr = []
    middle_arr = []
    right_arr = []
    pivot = random.choice(range(len(arr)))
    for item in arr:
        if item < arr[pivot]:
            left_arr.append(item)
        elif item == arr[pivot]:
            middle_arr.append(item)
        else:
            right_arr.append(item)
    return left_arr, middle_arr, right_arr


l = list(range(60))
rd.shuffle(l)
for i in range(1, 61):
    print(mom_select(l, i))

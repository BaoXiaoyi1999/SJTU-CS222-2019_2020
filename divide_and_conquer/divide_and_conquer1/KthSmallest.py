import random
import numpy as np


rd = random.Random()
rd.seed(0)


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


def quick_select_in_place_big(arr, k):
    return quick_select_in_place(arr, 0, len(arr)-1, k)


def quick_select_in_place(arr, lb, ub, k):
    left, middle, right = three_partition_in_place(arr, lb, ub)
    left_length = middle - left
    middle_length = right - middle
    right_length = ub - right + 1
    if k <= left_length:
        return quick_select_in_place(arr, left, middle-1, k)
    elif k > left_length + middle_length:
        return quick_select_in_place(arr, right, ub, k - left_length - middle_length)
    else:
        return arr[middle]


def three_partition_in_place(arr, lb, ub):
    pivot = random.choice(range(lb, ub+1))
    temp = arr[pivot]
    low = lb
    high = ub
    while low < high:
        while low < high and arr[low] <= arr[pivot]:
            low += 1
        while low < high and arr[high] > arr[pivot]:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]

    if arr[low] > arr[pivot]:
        arr[low-1], arr[pivot] = arr[pivot], arr[low-1]
    else:
        arr[low], arr[pivot] = arr[pivot], arr[low]

    left = lb
    middle = arr.index(temp)
    right = ub + 1
    for i in range(middle, ub+1):
        if arr[i] != temp:
            right = i
            break
    return left, middle, right


l = list(range(10))
rd.shuffle(l)
for i in range(1, 11):
    print(quick_select_in_place_big(l, i))


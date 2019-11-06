import random


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


def randomized_quick_sort_in_place_big(arr):
    randomized_quick_sort_in_place(arr, 0, len(arr) - 1)


def randomized_quick_sort_in_place(arr, lb, ub):
    if ub <= lb:
        return
    left, middle, right = three_partition_in_place(arr, lb, ub)
    randomized_quick_sort_in_place(arr, lb, middle-1)
    randomized_quick_sort_in_place(arr, right, ub)


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    left, middle, right = three_partition(arr)
    left_arr = randomized_quick_sort(left)
    middle_arr = randomized_quick_sort(middle)
    right_arr = randomized_quick_sort(right)
    full_arr = []
    full_arr.extend(left_arr)
    full_arr.extend(middle_arr)
    full_arr.extend(right_arr)
    return full_arr


def three_partition(arr):
    pivot = random.choice(range(len(arr)))
    left_arr = []
    middle_arr = []
    right_arr = []
    for item in arr:
        if item < arr[pivot]:
            left_arr.append(item)
        elif item == arr[pivot]:
            middle_arr.append(item)
        else:
            right_arr.append(item)
    return left_arr, middle_arr, right_arr


# the function shows that when list is passed as parameter, it works similarly to the pointer in cpp.
def modify(arr, index, target):
    arr[index] = target


rd = random.Random()
rd.seed(0)
l = list(range(20))
rd.shuffle(l)
print(l)
pivot_index = rd.choice(range(len(l)))
# l1 = randomized_quick_sort(l)
# print(l1)

l2 = l[:]
randomized_quick_sort_in_place_big(l2)
print(l2)

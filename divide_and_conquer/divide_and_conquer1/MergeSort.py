import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid_index = (len(arr) // 2)
        left_arr = merge_sort(arr[0:mid_index])
        right_arr = merge_sort(arr[mid_index:])
        res = merge(left_arr, right_arr)
        return res


def merge(left_arr, right_arr):
    res = []
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1
    res.extend(left_arr[i:])
    res.extend(right_arr[j:])
    return res


rd = random.Random()
rd.seed(0)

temp_list= list(range(0, 10))
rd.shuffle(temp_list)
print("temp_list: ", temp_list)
res = merge_sort(temp_list)
print("sorted_list:", res)

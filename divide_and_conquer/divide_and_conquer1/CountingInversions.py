def count_inversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid_index = len(arr) // 2
        left_arr, left_inv = count_inversions(arr[0: mid_index])
        right_arr, right_inv = count_inversions(arr[mid_index:])
        combined_arr, span_inv = calculate_span_inv(left_arr, right_arr)
        return combined_arr, left_inv + right_inv + span_inv


def calculate_span_inv(left_arr, right_arr):
    res = []
    i = 0
    j = 0
    counter = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        elif left_arr[i] == right_arr[j]:
            res.append(left_arr[i])
            res.append(right_arr[j])
            i += 1
            j += 1
        else:
            res.append(right_arr[j])
            j += 1
            counter += (len(left_arr) - i)
    res.extend(left_arr[i:])
    res.extend(right_arr[j:])
    return res, counter


def first_greater_index(arr, target):
    left = 0
    right = len(arr)
    while left != right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


input_l = [1, 5, 4, 8, 10, 2, 6, 9, 3, 7]
sorted_arr, total_inv = count_inversions(input_l)
print(sorted_arr, total_inv)

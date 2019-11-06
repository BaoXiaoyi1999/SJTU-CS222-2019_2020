import random
from math import sqrt


def closest_pair(arr):
    if len(arr) < 2:
        return None, 2
    elif len(arr) == 2:
        return (arr[0], arr[1]), calculate_distance(arr[0], arr[1])
    arr.sort()
    mid_index = int(len(arr) // 2)
    line = (arr[mid_index][0] + arr[mid_index + 1][0]) / 2  # line segment according to x coordinate
    selected_pair_left, distance_left = closest_pair(arr[0:mid_index])
    selected_pair_right, distance_right = closest_pair(arr[mid_index:])
    if distance_left < distance_right:
        smaller_distance = distance_left
        smaller_pair = selected_pair_left
    else:
        smaller_distance = distance_right
        smaller_pair = selected_pair_right

    remaining_points = []
    for point in arr:
        if abs(point[0] - line) <= smaller_distance:
            remaining_points.append(point)

    selected_pair = None
    selected_distance = 2
    remaining_points.sort(key=lambda item: item[1])
    for i in range(len(remaining_points)):
        for j in range(i+1, len(remaining_points)):
            if remaining_points[j][1] - remaining_points[i][1] > smaller_distance:
                break
            else:
                distance = calculate_distance(remaining_points[i], remaining_points[j])
                if distance < selected_distance:
                    selected_distance = distance
                    selected_pair = (remaining_points[i], remaining_points[j])

    if selected_distance < smaller_distance:
        return selected_pair, selected_distance
    else:
        return smaller_pair, smaller_distance


def closest_pair_brute_force(arr):
    greatest_distance = 2  # never reached
    selected_pair = None  # doesn't exist
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            temp = calculate_distance(arr[i], arr[j])
            if temp < greatest_distance:
                selected_pair = (arr[i], arr[j])
                greatest_distance = temp
    return selected_pair, greatest_distance


def calculate_distance(tuple1, tuple2):
    dx = tuple1[0] - tuple2[0]
    dy = tuple1[1] - tuple2[1]
    distance = sqrt(dx ** 2 + dy ** 2)
    return distance


def random_generator(length):
    rd = random.Random()
    rd.seed(0)
    res_arr = [(rd.random(), rd.random()) for i in range(length)]
    return res_arr


random_tuple = random_generator(100)
print(random_tuple)
cp_bf, dt_bf = closest_pair_brute_force(random_tuple)
cp_dc, dt_dc = closest_pair(random_tuple)
print(cp_bf, dt_bf)
print(cp_dc, dt_dc)

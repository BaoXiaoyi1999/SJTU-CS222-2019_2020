import random


random.seed(0)
# optimize the function E + cL


def generator(num_of_points):
    list_point = []
    pre_x = 0
    pre_y = 0
    for i in range(num_of_points):
        temp_x = pre_x + random.random()  # x is strictly increasing
        temp_y = pre_y + random.random() * 4 - 1   # (0, 1) -> (-1, 3)
        pre_x = temp_x
        pre_y = temp_y
        list_point.append((temp_x, temp_y))
    return list_point


class SegmentedLeastSquares:
    def __init__(self, list_point, c):
        self.list_point = list_point
        self.point_num = len(self.list_point)
        self.c = c
        self.opt = self.opt_min()

    def min_square_error(self, index_i, index_j):
        n = index_j - index_i + 1
        if n <= 1:
            return 0
        sum_x = sum([self.list_point[index][0] for index in range(index_i, index_j + 1)])
        sum_y = sum([self.list_point[index][1] for index in range(index_i, index_j + 1)])
        sum_x2 = sum([self.list_point[index][0] ** 2 for index in range(index_i, index_j + 1)])
        sum_xy = sum([self.list_point[index][0] * self.list_point[index][1] for index in range(index_i, index_j + 1)])
        a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        b = (sum_y - a * sum_x) / n
        error = sum([(a * self.list_point[index][0] + b - self.list_point[index][1])**2 for index in range(index_i, index_j + 1)])
        return error

    def opt_min(self):
        res_opt = [0]
        for j in range(1, self.point_num):
            temp_list = []
            for i in range(1, j+1):
                temp = self.min_square_error(i, j) + self.c + res_opt[i-1]
                temp_list.append(temp)
            res_opt.append(min(temp_list))
        return res_opt

    def display(self):
        print("opt_list:")
        print(self.opt)



point_num = 20
point_list = generator(point_num)
print(point_list)
for penalty in range(0, 50, 10):
    print("penelty = {0}".format(str(penalty)))
    solution = SegmentedLeastSquares(point_list, penalty)
    solution.display()
    print()


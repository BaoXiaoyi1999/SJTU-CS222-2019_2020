import numpy as np

# the code is unfinished. join point for those n * 2 stripes



class Hichberg:
    def __init__(self, str_x, str_y, gap_penalty=1, mismatch_penalty=1):
        self.str_x = str_x
        self.str_y = str_y
        self.len_x = len(str_x)
        self.len_y = len(str_y)
        self.gap_penalty = gap_penalty
        self.mismatch_penalty = mismatch_penalty
        self.res_list = []

    def alignment(self, str_x, str_y):
        len_x = len(str_x)
        len_y = len(str_y)
        opt_matrix = np.zeros(shape=(len_x+1, len_y+1))  # characters count from 1
        for i in range(len_x+1):  # when j == 0
            opt_matrix[i][0] = i * self.gap_penalty
        for j in range(len_y+1):  # when i == 0
            opt_matrix[0][j] = j * self.gap_penalty
        print("each case")
        for i in range(len_x):
            for j in range(len_y):
                case1 = self.pair_penalty(str_x, str_y, i, j) + opt_matrix[i][j]
                case2 = self.gap_penalty + opt_matrix[i][j+1]
                case3 = self.gap_penalty + opt_matrix[i+1][j]
                opt_matrix[i+1][j+1] = min(case1, case2, case3)
                print("tt")
        return opt_matrix

    def pair_penalty(self, str_x, str_y, i, j):
        # i, j: index of str, count from 0
        char1 = str_x[i]
        char2 = str_y[j]
        if char1 == char2:
            return 0
        else:
            return self.mismatch_penalty

    def divide_and_conquer_alignment(self, str_x, str_y, offset=(0, 0)):
        len_x = len(str_x)
        len_y = len(str_y)
        mid_col = len_y // 2
        # if len_x <= 2 or len_y <= 2:
        #     # use alignment to solve. to be continued.
        #     self.res_list.append((offset[0]+len_x)
        #     return
        if len_y == 2:
            self.alignment(str_x, str_y)
            #------need to decide the path and add to path list!!!!
            # self.res_list.append((offset[0]+len_x - 1, offset[1] + len_y - 1))
            return
        if len_y == 1:
            return
        list1 = self.space_efficient_opt(str_x, str_y[:mid_col])
        list2 = self.backward_space_efficient_opt(str_x, str_y[mid_col:])
        print(list1)
        print(list2)
        sum_list = [list1[i] + list2[i] for i in range(len(list1))]
        print(sum_list)
        q = sum_list.index(min(sum_list))
        self.res_list.append((q+offset[0], mid_col+offset[1]))  # absolute position?
        self.divide_and_conquer_alignment(str_x[:q+1], str_y[:mid_col+1], offset=(0, 0))
        self.divide_and_conquer_alignment(str_x[q:], str_y[mid_col:], offset=(q+offset[0], mid_col+offset[1]))
        print(self.res_list)

    def space_efficient_opt(self, str_x, str_y):
        len_x = len(str_x)
        len_y = len(str_y)
        opt_two_col = np.zeros(shape=(len_x+1, 2))
        for i in range(len_x + 1):  # when j == 0
            opt_two_col[i][0] = i * self.gap_penalty
        for j in range(len_y):
            # print(j)
            opt_two_col[0][1] = (j+1) * self.gap_penalty
            for i in range(len_x):
                case1 = self.pair_penalty(str_x, str_y, i, j) + opt_two_col[i][0]
                case2 = self.gap_penalty + opt_two_col[i][1]
                case3 = self.gap_penalty + opt_two_col[i+1][0]
                opt_two_col[i+1][1] = min(case1, case2, case3)
            # print(opt_two_col)
            for i in range(len_x + 1):
                opt_two_col[i][0] = opt_two_col[i][1]
            # print(opt_two_col)
        res = list(opt_two_col[:, 1])
        return res

    def backward_space_efficient_opt(self, str_x, str_y):
        str_x = str_x[::-1]
        str_y = str_y[::-1]
        temp = self.space_efficient_opt(str_x, str_y)
        temp.reverse()
        return temp



str1 = "ctaccg"
str2 = "tacatg"
solution = Hichberg(str1, str2)
solution.divide_and_conquer_alignment(str1, str2)
# for mid_col in range(6):
#     list1 = solution.space_efficient_opt(str1, str2[0:mid_col+1])
#     list2 = solution.backward_space_efficient_opt(str1, str2[mid_col+1:])
#     print(list1)
#     print(list2)
#     print()


# opt matrix:
# [[ 0.  1.  2.  3.  4.  5.  6.]
#  [ 1.  1.  2.  2.  3.  4.  5.]
#  [ 2.  1.  2.  3.  3.  3.  4.]
#  [ 3.  2.  1.  2.  3.  4.  4.]
#  [ 4.  3.  2.  1.  2.  3.  4.]
#  [ 5.  4.  3.  2.  2.  3.  4.]
#  [ 6.  5.  4.  3.  3.  3.  3.]]
# the result is:
# 3.0

#  opt matrix:(for reverse)
# [[ 0.  1.  2.  3.  4.  5.  6.]
#  [ 1.  0.  1.  2.  3.  4.  5.]
#  [ 2.  1.  1.  2.  2.  3.  4.]
#  [ 3.  2.  2.  2.  2.  3.  4.]
#  [ 4.  3.  3.  2.  3.  2.  3.]
#  [ 5.  4.  3.  3.  3.  3.  2.]
#  [ 6.  5.  4.  4.  3.  4.  3.]]
# the result is:

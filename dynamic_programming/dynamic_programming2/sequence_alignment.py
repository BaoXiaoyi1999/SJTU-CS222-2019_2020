import numpy as np


class SequenceAlignment:
    def __init__(self, str_x, str_y, gap_penalty=1, mismatch_penalty=1):
        self.str_x = str_x
        self.str_y = str_y
        self.len_x = len(str_x)
        self.len_y = len(str_y)
        self.gap_penalty = gap_penalty
        self.mismatch_penalty = mismatch_penalty

        self.opt_matrix = self.opt()


    def pair_penalty(self, i, j):
        # i, j: index of str, count from 0
        char1 = self.str_x[i]
        char2 = self.str_y[j]
        if char1 == char2:
            return 0
        else:
            return self.mismatch_penalty

    def opt(self):
        # add another row and column to indicate when one string is None
        opt_matrix = np.zeros(shape=(self.len_x+1, self.len_y+1))  # characters count from 1
        for i in range(self.len_x+1):  # when j == 0
            opt_matrix[i][0] = i * self.gap_penalty
        for j in range(self.len_y+1):  # when i == 0
            opt_matrix[0][j] = j * self.gap_penalty
        for i in range(self.len_x):
            for j in range(self.len_y):

                case1 = self.pair_penalty(i, j) + opt_matrix[i][j]
                case2 = self.gap_penalty + opt_matrix[i][j+1]
                case3 = self.gap_penalty + opt_matrix[i+1][j]
                # we may need another pointer matrix to indicate where it comes from,or just step back to the closest
                opt_matrix[i+1][j+1] = min(case1, case2, case3)
                # print(i, j)
                # print(opt_matrix)
        return opt_matrix

    def display(self):
        print("opt matrix:")
        print(self.opt_matrix)
        print("the result is:")
        print(self.opt_matrix[self.len_x][self.len_y])


str1 = "ctaccg"
str2 = "tacatg"
solution = SequenceAlignment(str1, str2)
solution.display()

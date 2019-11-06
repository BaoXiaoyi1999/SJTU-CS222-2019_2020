import random
import numpy as np

random.seed(0)


class Knapack:
    def __init__(self, weight_list, value_list, weight_limit):
        self.weight = weight_list  # weight are all integer numbers
        self.value = value_list
        self.num_of_elements = len(self.weight)  # suppose we have legal inpu
        self.weight_limit = weight_limit

        self.opt_matrix = self.opt()
        self.is_chosen = self.recover_solution()

    def opt(self):
        rows = self.num_of_elements+1
        cols = self.weight_limit+1
        opt_matrix = np.zeros(shape=(rows, cols))
        for weight in range(cols):
            opt_matrix[0][weight] = 0
        for i in range(1, rows):
            item_index = i-1
            for weight in range(1, cols):
                if self.weight[item_index] > weight:
                    opt_matrix[i][weight] = opt_matrix[i-1][weight]
                else:
                    take = opt_matrix[i-1][weight-self.weight[item_index]] + self.value[item_index]
                    leave = opt_matrix[i-1][weight]
                    opt_matrix[i][weight] = max(take, leave)
        return opt_matrix

    def recover_solution(self):
        chosen_list = []
        temp_row = self.num_of_elements
        temp_col = self.weight_limit   # represent the current weight left
        while temp_row > 0 and temp_col >= 0:
            print(temp_row, temp_col)
            if self.opt_matrix[temp_row][temp_col] == self.opt_matrix[temp_row-1][temp_col]:  # not chosen
                chosen_list.append(0)
            else:
                temp_weight = self.weight[temp_row-1]
                chosen_list.append(1)
                temp_col -= temp_weight
            temp_row -= 1
        while len(chosen_list) < self.num_of_elements:
            chosen_list.append(0)
        chosen_list.reverse()
        return chosen_list

    def display(self):
        print("weight list:", self.weight)
        print("value list:", self.value)

        print("opt matrix: ")
        print(self.opt_matrix)
        print("is chosen: ", self.is_chosen)
        print("optimal solution: ", self.opt_matrix[-1][-1])


all_weight = [1, 2, 5, 6, 7]
all_value = [1, 6, 18, 22, 28]
mapping = [(all_weight[i], all_value[i]) for i in range(len(all_value))]
random.shuffle(mapping)
print(mapping)
all_weight_new = [mapping[i][0] for i in range(len(all_value))]
all_value_new = [mapping[i][1] for i in range(len(all_value))]
capacity = 11
solution = Knapack(all_weight_new, all_value_new, capacity)
# solution = Knapack(all_weight, all_value, capacity)
solution.display()

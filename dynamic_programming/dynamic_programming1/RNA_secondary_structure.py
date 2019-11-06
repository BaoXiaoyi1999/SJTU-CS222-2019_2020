import numpy as np


class RNASecondaryStructure:
    def __init__(self, molecule):
        self.molecule = molecule
        self.length = len(molecule)
        self.matching = {"A": "U", "U": "A", "C": "G", "G": "C"}
        self.sharp_turn_threshold = 4
        self.opt_matrix = self.opt()

    def opt(self):
        rows = cols = self.length
        opt_matrix = np.zeros(shape=(rows, cols))
        # calculate from the substring of the smallest length
        for length in range(self.sharp_turn_threshold+1, self.length):
            for i in range(self.length - length):
                j = i + length
                choice1 = opt_matrix[i][j-1]
                choice2_list = [0]
                for t in range(i+1, j):
                    if self.molecule[t] == self.matching[self.molecule[j]]:  # t matches j
                        temp = 1 + opt_matrix[i][t-1] + opt_matrix[t+1][j-1]
                        choice2_list.append(temp)

                opt_matrix[i][j] = max(choice1, max(choice2_list))
        return opt_matrix

    def display(self):
        print(self.opt_matrix)
        print("max number of pairs = ", self.opt_matrix[0][-1])




RNA_str =  "GUCGAUUGAGCGAAUGUAACAACGUGGCUACGGCGAGA"
solution = RNASecondaryStructure(RNA_str)
solution.display()

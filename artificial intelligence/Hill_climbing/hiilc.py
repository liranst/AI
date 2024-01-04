import copy
import random
import random as rd
import numpy as np


def np_rd(n):
    number_list = list(range(1, n ** 2 + 1))
    rd.shuffle(number_list)
    matrix_rd = np.array(number_list).reshape((n, n))
    return matrix_rd


def random_step(new_mat):
    size = len(new_mat)
    i, j = random.randrange(size), random.randrange(size)
    x, y = random.randrange(size), random.randrange(size)
    new_mat[i][j], new_mat[x][y] = new_mat[x][y], new_mat[i][j]


def hill_climbing(n):
    start_mat = np_rd(n)
    best_matrix, best_det = start_mat, np.linalg.det(start_mat)

    for i in range(1000):
        new_matrix = copy.copy(best_matrix)
        random_step(new_matrix)
        new_dat = int(np.linalg.det(new_matrix))

        if new_dat >= best_det:
            best_matrix = new_matrix
            best_det = new_dat

    return best_matrix, best_det


best_mat, best_dat = hill_climbing(8)
print(f"best_dat =  {best_dat} \n "
      f"best_mat is: \n {best_mat}")
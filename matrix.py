class Matrix:
    def __init__(self, size_of_matrix, output_type):
        self.matrix_object = None
        self.size_of_matrix = size_of_matrix
        self.matrix_data = None
        self.output_type = output_type


class SquareMatrix:
    def __init__(self):
        self.type_of_matrix = 'Square Matrix'


def fill_square_matrix(matrix, matrix_data):
    numbers = str.split(matrix_data, ' ')
    tmp_matrix = [[0 for _ in range(matrix.size_of_matrix)] for _ in range(matrix.size_of_matrix)]
    k = 0
    for i in range(matrix.size_of_matrix):
        for j in range(matrix.size_of_matrix):
            tmp_matrix[i][j] = int(numbers[k])
            k += 1
    matrix.matrix_data = tmp_matrix


class SquareDiagonalMatrix:
    def __init__(self):
        self.type_of_matrix = 'Square Diagonal Matrix'


def fill_square_diagonal_matrix(matrix, matrix_data):
    numbers = str.split(matrix_data, ' ')
    tmp_matrix = [[0 for _ in range(matrix.size_of_matrix)] for _ in range(matrix.size_of_matrix)]
    k = 0
    for i in range(matrix.size_of_matrix):
        for j in range(matrix.size_of_matrix):
            if i == j:
                tmp_matrix[i][j] = int(numbers[k])
                k += 1
    matrix.matrix_data = tmp_matrix


def str_matrix(matrix):
    return f'\tType of Matrix = {matrix.matrix_object.type_of_matrix}\n' \
           f'\tSize of Matrix = {matrix.size_of_matrix}\n' \
           f'\tMatrix Data = {matrix.matrix_data}\n'


def get_output_type(matrix):
    return matrix.output_type


def print_matrix(matrix):
    out_str = f'\tType of Matrix = {matrix.matrix_object.type_of_matrix}\n' \
              f'\tSize of Matrix = {matrix.size_of_matrix}\n' \
              f'\tMatrix Data:\n'
    for i in range(matrix.size_of_matrix):
        out_str += f'\t'
        for j in range(matrix.size_of_matrix):
            if j != matrix.size_of_matrix - 1:
                out_str += f'{matrix.matrix_data[i][j]}\t'
            else:
                out_str += f'{matrix.matrix_data[i][j]}'
        out_str += f'\n'
    return out_str

class Matrix:
    """
    The source class for all matrices
    """
    def __init__(self, size_of_matrix, output_type):
        """
        Constructor of the Matrix class
        :param size_of_matrix: Size of the matrix
        :param output_type: Type of matrix output for printing
        """
        self.matrix_object = None
        self.size_of_matrix = size_of_matrix
        self.matrix_data = None
        self.output_type = output_type


class SquareMatrix:
    """
    Class for Square Matrix
    """
    def __init__(self):
        """
        Constructor of the Square Matrix class
        """
        self.type_of_matrix = 'Square Matrix'


def fill_square_matrix(matrix, matrix_data):
    """
    The function for filling a Square Matrix
    :param matrix: The matrix for filling
    :param matrix_data: Data for filling matrix
    """
    numbers = str.split(matrix_data, ' ')
    tmp_matrix = [[0 for _ in range(matrix.size_of_matrix)] for _ in range(matrix.size_of_matrix)]
    k = 0
    for i in range(matrix.size_of_matrix):
        for j in range(matrix.size_of_matrix):
            tmp_matrix[i][j] = int(numbers[k])
            k += 1
    matrix.matrix_data = tmp_matrix


class SquareDiagonalMatrix:
    """
    Class for Square Diagonal Matrix
    """
    def __init__(self):
        """
        Constructor of the Square Diagonal Matrix class
        """
        self.type_of_matrix = 'Square Diagonal Matrix'


def fill_square_diagonal_matrix(matrix, matrix_data):
    """
    The function for filling a Square Diagonal Matrix
    :param matrix: The matrix for filling
    :param matrix_data: Data for filling matrix
    """
    numbers = str.split(matrix_data, ' ')
    tmp_matrix = [[0 for _ in range(matrix.size_of_matrix)] for _ in range(matrix.size_of_matrix)]
    k = 0
    for i in range(matrix.size_of_matrix):
        for j in range(matrix.size_of_matrix):
            if i == j:
                tmp_matrix[i][j] = int(numbers[k])
                k += 1
    matrix.matrix_data = tmp_matrix


class LowerTriangularMatrix:
    """
    Class for Lower Triangular Matrix
    """
    def __init__(self):
        """
        Constructor of the Lower Triangular Matrix class
        """
        self.type_of_matrix = 'Lower Triangular Matrix'


def fill_lower_triangular_matrix(matrix, matrix_data):
    """
    The function for filling a Lower Triangular Matrix
    :param matrix: The matrix for filling
    :param matrix_data: Data for filling matrix
    """
    numbers = str.split(matrix_data, ' ')
    tmp_matrix = [[0 for _ in range(matrix.size_of_matrix)] for _ in range(matrix.size_of_matrix)]
    k = 0
    for i in range(matrix.size_of_matrix):
        for j in range(matrix.size_of_matrix):
            if i >= j:
                tmp_matrix[i][j] = int(numbers[k])
                k += 1
    matrix.matrix_data = tmp_matrix


def sum_of_all_matrix_elements(matrix):
    """
    The function in which the sum of all elements of the matrix is calculated
    :param matrix: Input matrix
    """
    all_sum = 0
    for i in range(matrix.size_of_matrix):
        for j in range(matrix.size_of_matrix):
            all_sum += matrix.matrix_data[i][j]
    return all_sum


def str_matrix(matrix):
    """
    The first type of matrix output for printing
    :param matrix: Input matrix
    """
    return f'\tType of Matrix = {matrix.matrix_object.type_of_matrix}\n' \
           f'\tSize of Matrix = {matrix.size_of_matrix}\n' \
           f'\tMatrix Data = {matrix.matrix_data}\n' \
           f'\tSum of all Elements = {sum_of_all_matrix_elements(matrix)}\n'


def compare(matrix1, matrix2):
    """
    The function in which two matrices are compared by the sum of all elements of the matrix
    :param matrix1: First matrix
    :param matrix2: Second Matrix
    """
    return sum_of_all_matrix_elements(matrix1) < sum_of_all_matrix_elements(matrix2)


def get_output_type(matrix):
    """
    The function which returns type of matrix
    :param matrix: Input matrix
    """
    return matrix.output_type


def print_matrix(matrix):
    """
    The second type of matrix output for printing
    :param matrix: Input matrix
    """
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
    out_str += f'\tSum of all Elements = {sum_of_all_matrix_elements(matrix)}\n'
    return out_str


def check(matrix_1, matrix_2):
    """
    The function that compares two classes of matrices
    :param matrix_1: First matrix for check
    :param matrix_2: Second matrix for check
    :return:
    """
    match matrix_1, matrix_2:
        case SquareMatrix(), SquareMatrix():
            print('Matrices belong to the same type: Square Matrix')
        case SquareMatrix(), SquareDiagonalMatrix():
            print('Matrices belong to the different types: Square Matrix and Square Diagonal Matrix')
        case SquareMatrix(), LowerTriangularMatrix():
            print('Matrices belong to the different types: Square Matrix and Lower Triangular Matrix')
        case SquareDiagonalMatrix(), SquareDiagonalMatrix():
            print('Matrices belong to the same type: Square Diagonal Matrix')
        case SquareDiagonalMatrix(), SquareMatrix():
            print('Matrices belong to the different types: Square Diagonal Matrix and Square Matrix')
        case SquareDiagonalMatrix(), LowerTriangularMatrix():
            print('Matrices belong to the different types: Square Diagonal Matrix and Lower Triangular Matrix')
        case LowerTriangularMatrix(), LowerTriangularMatrix():
            print('Matrices belong to the same type: Lower Triangular Matrix')
        case LowerTriangularMatrix(), SquareMatrix():
            print('Matrices belong to the different types: Lower Triangular Matrix and Square Matrix')
        case LowerTriangularMatrix(), SquareDiagonalMatrix():
            print('Matrices belong to the different types: Lower Triangular Matrix and Square Diagonal Matrix')
        case _:
            print('Unknown type')
            return

    print(f'First: type={type(matrix_1)}, id={id(matrix_1)}\nSecond: type={type(matrix_2)}, id={id(matrix_2)}\n')

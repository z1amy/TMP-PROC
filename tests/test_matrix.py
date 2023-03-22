from matrix import Matrix, SquareMatrix, fill_square_matrix, fill_square_diagonal_matrix,\
    fill_lower_triangular_matrix, sum_of_all_matrix_elements, print_matrix
from pytest import mark


@mark.parametrize('matrix_size,output_type,matrix_data,test_matrix_data',
                  [(3, 2, '1 2 3 4 5 6 7 8 9', [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   (2, 2, '0 6 7 10', [[0, 6], [7, 10]])])
def test_fill_square_matrix(matrix_size, output_type, matrix_data, test_matrix_data):
    matrix = Matrix(matrix_size, output_type)
    fill_square_matrix(matrix, matrix_data)

    assert matrix.matrix_data == test_matrix_data


@mark.parametrize('matrix_size,output_type,matrix_data,test_matrix_data',
                  [(3, 2, '1 2 3', [[1, 0, 0], [0, 2, 0], [0, 0, 3]]),
                   (2, 2, '0 6', [[0, 0], [0, 6]])])
def test_fill_square_diagonal_matrix(matrix_size, output_type, matrix_data, test_matrix_data):
    matrix = Matrix(matrix_size, output_type)
    fill_square_diagonal_matrix(matrix, matrix_data)

    assert matrix.matrix_data == test_matrix_data


@mark.parametrize('matrix_size,output_type,matrix_data,test_matrix_data',
                  [(3, 2, '1 2 3 4 5 6', [[1, 0, 0], [2, 3, 0], [4, 5, 6]]),
                   (2, 2, '0 6 7', [[0, 0], [6, 7]])])
def test_fill_lower_triangular_matrix(matrix_size, output_type, matrix_data, test_matrix_data):
    matrix = Matrix(matrix_size, output_type)
    fill_lower_triangular_matrix(matrix, matrix_data)

    assert matrix.matrix_data == test_matrix_data


@mark.parametrize('matrix_size,output_type,matrix_data,test_sum_matrix',
                  [(3, 2, '1 2 3 4 5 6 7 8 9', 45),
                   (2, 2, '0 6 7 10', 23)])
def test_sum_of_all_matrix_elements(matrix_size, output_type, matrix_data, test_sum_matrix):
    matrix = Matrix(matrix_size, output_type)
    fill_square_matrix(matrix, matrix_data)

    assert sum_of_all_matrix_elements(matrix) == test_sum_matrix


@mark.parametrize('matrix_size,output_type,matrix_data,test_str_matrix',
                  [(3, 2, '1 2 3 4 5 6 7 8 9', '\tType of Matrix = Square Matrix\n' \
                                               '\tSize of Matrix = 3\n' \
                                               '\tMatrix Data:\n' \
                                               '\t1\t2\t3\n' \
                                               '\t4\t5\t6\n' \
                                               '\t7\t8\t9\n' \
                                               '\tSum of all Elements = 45\n'),
                   (2, 2, '0 6 7 10', '\tType of Matrix = Square Matrix\n' \
                                      '\tSize of Matrix = 2\n' \
                                      '\tMatrix Data:\n' \
                                      '\t0\t6\n' \
                                      '\t7\t10\n' \
                                      '\tSum of all Elements = 23\n')])
def test_print_matrix(matrix_size, output_type, matrix_data, test_str_matrix):
    matrix = Matrix(matrix_size, output_type)
    matrix.matrix_object = SquareMatrix()
    fill_square_matrix(matrix, matrix_data)

    assert print_matrix(matrix) == test_str_matrix

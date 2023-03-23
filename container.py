from matrix import Matrix, SquareMatrix, SquareDiagonalMatrix, LowerTriangularMatrix, str_matrix, fill_square_matrix, \
    fill_square_diagonal_matrix, fill_lower_triangular_matrix, get_output_type, print_matrix, compare, check
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


def clear(container):
    container.__init__()


def get_size(container):
    return container.size


def add(container, data):
    new_node = Node(data)
    if container.head is None:
        container.head = new_node
        container.tail = new_node
        new_node.next = container.head
    else:
        container.tail.next = new_node
        container.tail = new_node
        container.tail.next = container.head
    container.size += 1


def read_from_file(container, in_file):
    try:
        lines = in_file.readlines()
    except OSError:
        print(f'File reading error {in_file}!')
        sys.exit(1)

    if len(lines) % 4 != 0:
        print('Invalid input data format!')
        sys.exit(1)

    for index in range(0, len(lines), 4):
        try:
            type_of_matrix = int(lines[index].strip())
            size_of_matrix = int(lines[index + 1].strip())
            output_type = int(lines[index + 2].strip())
        except ValueError:
            print('Invalid input data format!')
            sys.exit(1)
        matrix_data = lines[index + 3].strip()
        new_matrix = None
        if type_of_matrix == 1:
            new_matrix = Matrix(size_of_matrix, output_type)
            new_matrix.matrix_object = SquareMatrix()
            try:
                fill_square_matrix(new_matrix, matrix_data)
            except IndexError or ValueError:
                print('Invalid input data format!')
                sys.exit(1)
        elif type_of_matrix == 2:
            new_matrix = Matrix(size_of_matrix, output_type)
            new_matrix.matrix_object = SquareDiagonalMatrix()
            try:
                fill_square_diagonal_matrix(new_matrix, matrix_data)
            except IndexError or ValueError:
                print('Invalid input data format!')
                sys.exit(1)
        elif type_of_matrix == 3:
            new_matrix = Matrix(size_of_matrix, output_type)
            new_matrix.matrix_object = LowerTriangularMatrix()
            try:
                fill_lower_triangular_matrix(new_matrix, matrix_data)
            except IndexError or ValueError:
                print('Invalid input data format!')
                sys.exit(1)
        add(container, new_matrix)


def write_to_file(container, out_file):
    current = container.head
    try:
        if container.head is None:
            out_file.write('Container is empty!\n')
        else:
            i = 0
            out_file.write('Filled Container:\n')
            if get_output_type(current.data) == 1:
                out_file.write(f'{i}: {str(print_matrix(current.data))}')
            else:
                out_file.write(f'{i}: {str_matrix(current.data)}')
            while current.next != container.head:
                i += 1
                current = current.next
                if get_output_type(current.data) == 1:
                    out_file.write(f'{i}: {str(print_matrix(current.data))}')
                else:
                    out_file.write(f'{i}: {str_matrix(current.data)}')
        out_file.write(f'Container contains {get_size(container)} elements.\n')
    except OSError:
        print(f'File writing error {out_file}!')
        sys.exit(1)


def filtered_write_to_file(container, out_file):
    current = container.head
    try:
        if container.head is None:
            out_file.write('Container is empty!\n')
        else:
            i = 0
            out_file.write('Filled Container:\n')
            if current.data.matrix_object.type_of_matrix == 'Square Matrix':
                if get_output_type(current.data) == 1:
                    out_file.write(f'{i}: {str(print_matrix(current.data))}')
                else:
                    out_file.write(f'{i}: {str_matrix(current.data)}')
            while current.next != container.head:
                i += 1
                current = current.next
                if current.data.matrix_object.type_of_matrix == 'Square Matrix':
                    if get_output_type(current.data) == 1:
                        out_file.write(f'{i}: {str(print_matrix(current.data))}')
                    else:
                        out_file.write(f'{i}: {str_matrix(current.data)}')
        out_file.write(f'Container contains {get_size(container)} elements.\n')
    except OSError:
        print(f'File writing error {out_file}!')
        sys.exit(1)


def sort(container):
    if container.head is not None:
        node1 = container.head
        node2 = container.head.next
        while True:
            while True:
                if compare(node1.data, node2.data):
                    node1.data, node2.data = node2.data, node1.data
                node2 = node2.next
                if node2 is container.head:
                    break
            node1 = node1.next
            node2 = container.head
            if node1 is container.head:
                break


def check_matrices(container):
    node1 = container.head
    while True:
        node2 = container.head
        while True:
            check(node1.data.matrix_object, node2.data.matrix_object)
            node2 = node2.next
            if node2 == container.head:
                break
        node1 = node1.next
        if node1 == container.head:
            break

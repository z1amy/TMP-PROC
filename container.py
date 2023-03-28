from matrix import Matrix, SquareMatrix, SquareDiagonalMatrix, LowerTriangularMatrix, str_matrix, fill_square_matrix, \
    fill_square_diagonal_matrix, fill_lower_triangular_matrix, get_output_type, print_matrix, compare, check
import sys


class Node:
    """
    Class describing the node of Circular Linked List
    """
    def __init__(self, data):
        """
        Constructor of the Node class
        :param data: The data contained in the class (matrix)
        """
        self.data = data
        self.next = None


class CircularLinkedList:
    """
    Class representing the implementation of the container (Circular Linked List)
    """
    def __init__(self):
        """
        Constructor of the Circular Linked List class
        """
        self.size = 0
        self.head = None
        self.tail = None


def clear(container):
    """
    The function which cleans the container
    :param container: Circular Linked List
    """
    container.__init__()


def get_size(container):
    """
    The function which returns the length of the container
    :param container: Circular Linked List
    """
    return container.size


def add(container, data):
    """
    The function which adds new node to the container
    :param container: Circular Linked List
    :param data: The data contained in the new node
    """
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
    """
    The function in which the file is read and the container is filled
    :param container: Circular Linked List
    :param in_file: Input file
    """
    for line in in_file:
        data = line.strip().split(';')
        try:
            type_of_matrix = int(data[0].strip())
            size_of_matrix = int(data[1].strip())
            output_type = int(data[2].strip())
        except ValueError:
            print(f'Invalid input data format!\n'
                  f'Line: {line}\n')
            continue
        matrix_data = data[3].strip()
        if type_of_matrix == 1:
            new_matrix = Matrix(size_of_matrix, output_type)
            new_matrix.matrix_object = SquareMatrix()
            try:
                fill_square_matrix(new_matrix, matrix_data)
            except (IndexError, ValueError):
                print(f'Invalid input data format!\n'
                      f'Line: {line}\n')
                continue
        elif type_of_matrix == 2:
            new_matrix = Matrix(size_of_matrix, output_type)
            new_matrix.matrix_object = SquareDiagonalMatrix()
            try:
                fill_square_diagonal_matrix(new_matrix, matrix_data)
            except (IndexError, ValueError):
                print(f'Invalid input data format!\n'
                      f'Line: {line}\n')
                continue
        elif type_of_matrix == 3:
            new_matrix = Matrix(size_of_matrix, output_type)
            new_matrix.matrix_object = LowerTriangularMatrix()
            try:
                fill_lower_triangular_matrix(new_matrix, matrix_data)
            except (IndexError, ValueError):
                print(f'Invalid input data format!\n'
                      f'Line: {line}\n')
                continue
        else:
            continue
        add(container, new_matrix)


def write_to_file(container, out_file):
    """
    The function in which the container is written to the file
    :param container: Circular Linked List
    :param out_file: Output file
    """
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
    """
    The function in which the filtered container is written to the file
    Only square matrices are written
    :param container: Circular Linked List
    :param out_file: Output file
    """
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
    """
    The function in which the container is sorted
    :param container: Circular Linked List
    """
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
    """
    The function in which container nodes are compared
    :param container: Circular Linked List
    """
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

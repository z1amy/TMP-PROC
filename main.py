import sys
import container


def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = 'in.txt'
        output_file = 'out.txt'

    cl = container.CircularLinkedList()

    with open(input_file, 'r') as in_file:
        container.read_from_file(cl, in_file)

    with open(output_file, 'w') as out_file:
        container.write_to_file(cl, out_file)

    with open(output_file, 'a') as out_file:
        container.clear(cl)
        container.write_to_file(cl, out_file)


if __name__ == '__main__':
    main()

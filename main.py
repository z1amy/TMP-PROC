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

    try:
        with open(input_file, 'r') as in_file:
            container.read_from_file(cl, in_file)
    except OSError:
        print(f'File opening error {in_file}!')
        sys.exit(1)

    container.sort(cl)
    container.check_matrices(cl)

    try:
        with open(output_file, 'w') as out_file:
            # container.filtered_write_to_file(cl, out_file)
            container.write_to_file(cl, out_file)

        with open(output_file, 'a') as out_file:
            container.clear(cl)
            # container.filtered_write_to_file(cl, out_file)
            container.write_to_file(cl, out_file)
    except OSError:
        print(f'File writing error {out_file}!')
        sys.exit(1)


if __name__ == '__main__':
    main()

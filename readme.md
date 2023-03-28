# Programming technologies and methods. Procedural Style

---

# Variant

| Task | №3 |
| --- | --- |
| Container | №3 |
| Module | №2 |
| Union | №2 |

# To run program you need to write in the terminal:

```bash
python main.py in.txt out.txt
```

# Modules

All files included in the project are described here.

## container.py

This file contains the implementation of circular linked list.

## matrix.py

This file describes the types of matrices and their implementation.

## in.txt and out.txt

These files are used to enter data into the program and to output processed data from it.

When you run program, you should specify these files.

If you do not do this, program will use default files:

```bash
in.txt and out.txt
```

Input data should be written in the following style:

```bash
Type_of_matrix(int);Size_of_matrix(int);Output_type(int);Data_for_matrix(array_of_int)
```

Here are some examples of input and output data:

```bash
in.txt:
1;4;1;1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
out.txt:
Type of Matrix = Square Matrix
Size of Matrix = 4
Matrix Data:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
Sum of all Elements = 136

in.txt:
2;2;1;1 1
out.txt:
Type of Matrix = Square Diagonal Matrix
Size of Matrix = 2
Matrix Data:
1	0
0	1

in.txt:
2;3;2;4 5 6
out.txt:
Type of Matrix = Square Diagonal Matrix
Size of Matrix = 3
Matrix Data = [[4, 0, 0], [0, 5, 0], [0, 0, 6]]
Sum of all Elements = 15

in.txt:
3;3;1;1 2 3 4 5 6
out.txt:
Type of Matrix = Lower Triangular Matrix
Size of Matrix = 3
Matrix Data:
1	0	0
2	3	0
4	5	6
Sum of all Elements = 21
```

## tests

This folder contains functions for testing.

To run tests you need to go to the folder tests and write in the terminal:

```bash
pytest
```
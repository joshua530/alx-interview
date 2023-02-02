#!/usr/bin/env python3
def solve_n_queens(n):
    positive_diags = set()
    negative_diags = set()
    cols = []

    def traverse(row):
        if row == n:
            # we've reached the end row & found n number of queens
            # print the found positions
            print("[", end="")
            for row in range(n):
                print("[{}, {}]".format(row, cols[row]), end="")
                if row != n - 1:
                    print(", ", end="")
            print("]")
            return
        for col in range(n):
            if col in cols or (row + col) in positive_diags or (row - col) in negative_diags:
                continue
            cols.append(col)
            positive_diags.add(row + col)
            negative_diags.add(row - col)

            traverse(row + 1)

            # backtrack
            positive_diags.remove(row + col)
            negative_diags.remove(row - col)
            cols.pop()
    traverse(0)

solve_n_queens(4)

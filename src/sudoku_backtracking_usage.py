from backtracking.imp.sudoku_backtracking.sudoku_backtracking import SudokuBacktracking

sudoku_1_solution = [[6, 0, 9, 0, 0, 0, 0, 0, 8],
                     [0, 0, 0, 3, 0, 1, 0, 0, 0],
                     [4, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 6, 0, 0, 0, 4],
                     [0, 2, 0, 0, 0, 0, 0, 3, 0],
                     [0, 7, 0, 0, 0, 0, 5, 0, 0],
                     [0, 1, 0, 5, 0, 0, 0, 7, 0],
                     [8, 0, 0, 0, 9, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 2, 0, 0]]

sudoku_n_solutions = [[0, 7, 0, 0, 2, 0, 0, 5, 0],
                      [0, 0, 3, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 3, 0, 9, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [4, 0, 0, 0, 0, 0, 0, 9, 0],
                      [0, 0, 0, 1, 7, 0, 0, 0, 3],
                      [0, 0, 5, 0, 0, 0, 0, 0, 7],
                      [3, 0, 0, 0, 8, 6, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0]]

sudoku_backtracking = SudokuBacktracking(sudoku_1_solution)
for solution in sudoku_backtracking.solve_all_solutions():
    print(solution)

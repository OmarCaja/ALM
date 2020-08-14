from backtracking.imp.n_queens_backtracking.n_queens_backtracking import NQueensBacktracking

nQueens = NQueensBacktracking([-1, -1, -1, -1, -1, -1])
for solution in nQueens.solve_all_solutions():
    print(solution)

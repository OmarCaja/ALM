from backtracking.imp.n_queens_backtracking.n_queens_backtracking import NQueensBacktracking

print('First solution')
nQueens = NQueensBacktracking([-1, -1, 4, -1, -1])
print(nQueens.solve())

print('All solutions')
nQueens = NQueensBacktracking([-1, -1, 4, -1, -1])
for solution in nQueens.solve_all_solutions():
    print(solution)

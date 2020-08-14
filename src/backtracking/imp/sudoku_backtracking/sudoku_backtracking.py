from backtracking.backtracking import Backtracking


class SudokuBacktracking(Backtracking):

    def __init__(self, sudoku):
        self.__sudoku = sudoku
        self.__nodes_to_explore = [[i, j] for i in range(len(sudoku)) for j in range(len(sudoku))
                                   if self.sudoku[i][j] == 0]

    @property
    def sudoku(self):
        return self.__sudoku

    @sudoku.setter
    def sudoku(self, sudoku):
        self.__sudoku = sudoku

    @property
    def nodes_to_explore(self):
        return self.__nodes_to_explore

    def _is_solution(self):
        return not self.nodes_to_explore

    def __can_insert_in_cell(self, number_to_insert, row, column):
        return self.__can_insert_in_row(number_to_insert, row) and \
               self.__can_insert_in_column(number_to_insert, column) and \
               self.__can_insert_in_matrix(number_to_insert, row, column)

    def __can_insert_in_row(self, number_to_insert, row):
        for number in self.sudoku[row]:
            if number == number_to_insert:
                return False
        return True

    def __can_insert_in_column(self, number_to_insert, column):
        for row in range(len(self.sudoku)):
            if self.sudoku[row][column] == number_to_insert:
                return False
        return True

    def __can_insert_in_matrix(self, number_to_insert, row, column):
        row_matrix_range = self.__calculate_matrix_range(row)
        column_matrix_range = self.__calculate_matrix_range(column)

        for row in range(row_matrix_range[0], row_matrix_range[1]):
            for column in range(column_matrix_range[0], column_matrix_range[1]):
                if self.sudoku[row][column] == number_to_insert:
                    return False
        return True

    @staticmethod
    def __calculate_matrix_range(index):
        init_position = index - (index % 3)
        return [init_position, init_position + 3]

    def _is_promising(self, number_to_insert, row, column):
        return self.__can_insert_in_cell(number_to_insert, row, column)

    def _backtracking(self):
        if self._is_solution():
            return self.sudoku
        else:
            pos = self.nodes_to_explore.pop(0)
            row = pos[0]
            column = pos[1]
            for number_to_insert in range(1, 10):
                if self._is_promising(number_to_insert, row, column):
                    self.sudoku[row][column] = number_to_insert
                    solution = self._backtracking()
                    if solution is not None:
                        return solution
            self.sudoku[row][column] = 0
            self.nodes_to_explore.insert(0, pos)
            return None

    def solve(self):
        return self._backtracking()

    def _backtracking_all_solutions(self):
        if self._is_solution():
            yield self.sudoku
        else:
            pos = self.nodes_to_explore.pop(0)
            row = pos[0]
            column = pos[1]
            for number_to_insert in range(1, 10):
                if self._is_promising(number_to_insert, row, column):
                    self.sudoku[row][column] = number_to_insert
                    for solution in self._backtracking_all_solutions():
                        yield solution
            self.sudoku[row][column] = 0
            self.nodes_to_explore.insert(0, pos)

    def solve_all_solutions(self):
        return self._backtracking_all_solutions()

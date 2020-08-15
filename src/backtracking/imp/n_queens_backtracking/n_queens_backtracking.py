from backtracking.backtracking import Backtracking


class NQueensBacktracking(Backtracking):

    def __init__(self, board=None):
        if board is None:
            board = [-1, -1, -1, -1]
        self.__board = board
        self.__nodes_to_explore = [pos for pos in range(len(board)) if board[pos] == -1]

    @property
    def board(self):
        return self.__board

    @property
    def nodes_to_explore(self):
        return self.__nodes_to_explore

    def _is_solution(self):
        return not self.nodes_to_explore

    def _is_promising(self, value, pos):
        return self.__are_all_queens_in_different_rows(value) and \
               self.__are_all_queens_in_different_diagonals(value, pos)

    def __are_all_queens_in_different_rows(self, value):
        for index in range(len(self.board)):
            if self.board[index] != -1 and self.board[index] == value:
                return False
        return True

    def __are_all_queens_in_different_diagonals(self, value, pos):
        for index in range(len(self.board)):
            if self.board[index] != -1 and abs(self.board[index] - value) == abs(pos - index):
                return False
        return True

    def _backtracking(self):
        if self._is_solution():
            return self.board
        else:
            pos = self.nodes_to_explore.pop(0)
            for value in range(len(self.board)):
                if self._is_promising(value, pos):
                    self.board[pos] = value
                    solution = self._backtracking()
                    if solution is not None:
                        return solution
            self.board[pos] = -1
            self.nodes_to_explore.insert(0, pos)
            return None

    def solve(self):
        return self._backtracking()

    def _backtracking_all_solutions(self):
        if self._is_solution():
            yield self.board
        else:
            pos = self.nodes_to_explore.pop(0)
            for value in range(len(self.board)):
                if self._is_promising(value, pos):
                    self.board[pos] = value
                    for solution in self._backtracking_all_solutions():
                        yield solution
            self.board[pos] = -1
            self.nodes_to_explore.insert(0, pos)

    def solve_all_solutions(self):
        return self._backtracking_all_solutions()

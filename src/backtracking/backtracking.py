import abc


class Backtracking(abc.ABC):
    @abc.abstractmethod
    def _is_solution(self, *args):
        pass

    @abc.abstractmethod
    def _is_promising(self, *args):
        pass

    @abc.abstractmethod
    def _backtracking(self, *args):
        pass

    @abc.abstractmethod
    def solve(self):
        pass

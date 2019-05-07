from typing import List, Tuple
from ..types import StrArray2D
from flask import current_app


class NeighborsHelper:
    """
    i = row
    j = col
    """

    def __init__(self, board: StrArray2D):
        self.board = board

    def get_neighbors(self, path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        i, j = path[-1]
        neighbors = [
            self._up(i, j),
            self._upper_right(i, j),
            self._right(i, j),
            self._lower_right(i, j),
            self._down(i, j),
            self._lower_left(i, j),
            self._left(i, j),
            self._upper_left(i, j)
        ]
        return list(
            filter(
                lambda n: n not in path,
                filter(lambda n: not self._is_off_limits(n), neighbors)
            )
        )

    def _is_off_limits(self, n: Tuple[int, int]):
        i, j = n
        board_size = len(self.board)
        if (i < 0 or j < 0 or i >= board_size or j >= board_size):
            return True
        return False

    def _up(self, i, j): return (i-1, j)

    def _upper_right(self, i, j): return (i-1, j+1)

    def _right(self, i, j): return (i, j+1)

    def _lower_right(self, i, j): return (i+1, j+1)

    def _down(self, i, j): return (i+1, j)

    def _lower_left(self, i, j): return (i+1, j-1)

    def _left(self, i, j): return (i, j-1)

    def _upper_left(self, i, j): return (i-1, j-1)

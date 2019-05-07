from flask import current_app
from ..word_dictionary import WordDictionary
from typing import List
from ..types import StrArray2D, SearchResult


def validate_board(b: StrArray2D) -> bool:
    rows: int = len(b)
    if rows == 0:
        return False
    for i in range(0, rows):
        col = b[i]
        if len(col) != rows:
            return False
    return True


def solve(board: StrArray2D) -> SearchResult:
    is_valid = validate_board(board)
    if not is_valid:
        raise Exception("Invalid board format")

    word_dictionary = WordDictionary()
    return word_dictionary.find_words(board)

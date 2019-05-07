from flask import current_app
from typing import List, Tuple
from ..types import StrArray2D, SearchResult, Word
from werkzeug.contrib.cache import SimpleCache
from .neighbors_helper import NeighborsHelper


cache = SimpleCache()


class WordDictionary:
    def __init__(self):
        word_dictionary: List[str] = cache.get('dictionary')

        if word_dictionary is not None:
            current_app.logger.info("Reading dictionary from cache...")
        else:
            current_app.logger.info("Reading dictionary from file...")
            f = open('dictionary.txt', 'r')
            word_dictionary: List[str] = f.read().splitlines()
            f.close()
            cache.set('dictionary', word_dictionary)

        current_app.logger.info("Dictionary read!")

        self.dictionary = word_dictionary

    def find_words(self, board: StrArray2D) -> SearchResult:
        result: SearchResult = []
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                words = self._look_for_words(board, i, j)
                if words:
                    result.extend(words)
        return {
            "words": result,
            "total_points": sum([word["points"] for word in result])
        }

    def _look_for_words(self, board: StrArray2D, i: int, j: int) -> SearchResult:
        neighbors_helper = NeighborsHelper(board)

        def lookup(accumulator: SearchResult,
                   path: List[Tuple[int, int]],
                   current_word='',
                   results=[]):
            if self._is_match(current_word, results):
                accumulator.append(self._format_word(
                    current_word, path, board))

            for n in neighbors_helper.get_neighbors(path):
                next_path = [*path, n]
                next_word = self._create_word(board, next_path)
                next_results = self._search_on_dictionary(next_word, results)
                if len(next_results) >= 1:
                    accumulator = lookup(
                        accumulator, next_path, next_word, next_results)

            return accumulator

        return lookup(accumulator=[], path=[(i, j)])

    def _create_word(self, board: StrArray2D, path: List[Tuple[int, int]]) -> str:
        return ''.join([c for c in map(lambda p: board[p[0]][p[1]], path)])

    def _search_on_dictionary(self, criteria: str, partial_results=[]) -> List[str]:
        dictionary = partial_results or self.dictionary
        return [word for word in dictionary if word.startswith(criteria)]

    def _is_match(self, word: str, results: List[str]) -> bool:
        if len(results) < 1 or len(word) < 3:
            return False
        return word in results

    def _format_word(self, word: str, path: List[Tuple[int, int]], board: StrArray2D) -> Word:
        letters = []
        last_point = None
        for i in range(len(path)-1, -1, -1):
            k, v = path[i]
            letters.append({
                "value": board[k][v],
                "coordinates": (k, v),
                "next_coordinates":  last_point
            })
            last_point = (k, v)

        return {
            "value": word,
            "points": self._get_score(word),
            "letters": letters
        }

    def _get_score(self, word: str) -> int:
        word_length = len(word)
        if word_length >= 8:
            return 11
        if word_length == 7:
            return 5
        if word_length == 6:
            return 3
        if word_length == 5:
            return 2
        if word_length == 4 or word_length == 3:
            return 1
        return 0

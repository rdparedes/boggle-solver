from typing import List, Dict, Tuple, Union

StrArray2D = List[List[str]]
Letter = Dict[str, Union[str, Tuple[int, int]]]
Word = Dict[str, Union[str, List[Letter]]]
SearchResult = List[Word]

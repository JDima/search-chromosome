import pytest
from typing import List, Tuple
from search_chromosome.search_chromosome import search_chromosome


class Case:
    def __init__(self, name: str, sv_bounds: List[Tuple[int, int]], k_conditions: List[Tuple[int, int]],
                 l_conditions: List[Tuple[int, int]], chromosomes):
        self.name = name
        self.sv_bounds = sv_bounds
        self.k_conditions = k_conditions
        self.l_conditions = l_conditions
        self.chromosomes = chromosomes

    def __str__(self) -> str:
        return 'sv_test/{}'.format(self.name)


SEARCH_CHROMOSOME_TEST_CASES = [
    Case(name="1 chr 1 SV no cond",
         sv_bounds=[(1, 1)],
         k_conditions=[],
         l_conditions=[],
         chromosomes=[1]
         ),
    Case(name="1 chr 2 SV no cond",
         sv_bounds=[(1, 1), (1, 1)],
         k_conditions=[],
         l_conditions=[],
         chromosomes=[1]
         ),
    Case(name="1 chr 1 K-cond",
         sv_bounds=[(1, 1), (1, 1)],
         k_conditions=[(1, 2)],
         l_conditions=[],
         chromosomes=[1]
         ),
    Case(name="1 chr 1 L-cond",
         sv_bounds=[(1, 1), (1, 1)],
         k_conditions=[],
         l_conditions=[(1, 2)],
         chromosomes=None
         ),
    Case(name="two chromosome",
         sv_bounds=[(1, 2), (2, 3)],
         k_conditions=[(1, 2)],
         l_conditions=[(1, 2)],
         chromosomes=[1, 3]
         ),
    Case(name="basic",
         sv_bounds=[(1, 3), (2, 10), (3, 5), (8, 9)],
         k_conditions=[(1, 2), (3, 4)],
         l_conditions=[(1, 3)],
         chromosomes=[4, 5, 8, 9]
         ),
    Case(name="some svs must be unused",
         sv_bounds=[(1, 10), (1, 10), (1, 10), (1, 10)],
         k_conditions=[(1, 2), (3, 4)],
         l_conditions=[(1, 3)],
         chromosomes=None),
    Case(name="controversial conditions",
         sv_bounds=[(1, 3), (1, 3), (1, 3), (1, 3), (4, 5)],
         k_conditions=[(1, 2), (3, 3)],
         l_conditions=[(1, 2)],
         chromosomes=None),
    Case(name="no constraints non first chr",
         sv_bounds=[(2, 5)],
         k_conditions=[],
         l_conditions=[],
         chromosomes=[2, 3, 4, 5]),
    Case(name="K constraints only",
         sv_bounds=[(2, 5), (5, 7)],
         k_conditions=[(1, 1), (1, 2), (2, 2)],
         l_conditions=[],
         chromosomes=[5]),
    Case(name="L constraints only",
         sv_bounds=[(2, 5), (5, 7), (6, 7), (4, 6), (1, 3), (1, 4)],
         k_conditions=[],
         l_conditions=[(1, 3), (2, 4), (5, 6)],
         chromosomes=[4, 7]),
    Case(name="one possible answer",
         sv_bounds=[(1, 2), (2, 7), (9, 11), (12, 15), (12, 14), (7, 11), (15, 15)],
         k_conditions=[(2, 4), (2, 7), (3, 4)],
         l_conditions=[(1, 2), (4, 5), (3, 6), (3, 7)],
         chromosomes=[15]),
    Case(name="no good chromosomes",
         sv_bounds=[(1, 2), (2, 7), (9, 11), (12, 15), (12, 14), (7, 11), (9, 11)],
         k_conditions=[(2, 4), (2, 7), (3, 4)],
         l_conditions=[(1, 2), (4, 5), (3, 6), (3, 7)],
         chromosomes=None),
    Case(name="unused SVs",
         sv_bounds=[(1, 2), (2, 7), (9, 11), (12, 15), (12, 14), (7, 11), (9, 15), (1, 2), (3, 3), (8, 13), (1, 15)],
         k_conditions=[(2, 7), (3, 4)],
         l_conditions=[(1, 2), (4, 5), (3, 6)],
         chromosomes=[15]),
]


@pytest.mark.parametrize('case', SEARCH_CHROMOSOME_TEST_CASES, ids=str)
def test_search_chromosome(case: Case) -> None:
    answer = search_chromosome(case.sv_bounds, case.k_conditions, case.l_conditions)
    if case.chromosomes is None:
        assert answer is None
    else:
        assert answer in case.chromosomes

#!/usr/bin/env python3
import csv
import math
from typing import List

from typing import Tuple
"""Compute pagnation"""


def index_range(page: int, page_size: int) -> Tuple:

    """A funtion to compute pagenation based of the args
        Arg:
            page (int) page number
            page_size (Int) number of rows
    """
    if page == 1:
        start_index = 0
    start_index = (page - 1) * page_size + 1
    end = start_index + page_size - 1

    return (start_index - 1, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index = index_range(page, page_size)
        sets = []

        for i in index:
            if i > len(self.dataset()):
                return []
            sets.append(self.dataset()[i])
        return sets

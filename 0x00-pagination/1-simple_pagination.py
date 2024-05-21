#!/usr/bin/env python3
"""Compute pagnation"""
import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:

    """
    A funtion to compute pagenation based of the args
        Arg:
            page (int) page number
            page_size (Int) number of rows
    Return:
        tuple of range of index
    """

    start_next_index = page * page_size
    start_index = start_next_index - page_size
    return (start_index, start_next_index)


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
        """
        Get the data from data set based on range of tuple
            Args:
                page (int): page number
                page_size (int): number of items pair page
            Return:
                dict of items
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index = index_range(page, page_size)
        sets = []
        i = index[0]
        while(i < index[-1]):
            if i > len(self.dataset()):
                return []
            sets.append(self.dataset()[i])
            i += 1
        return sets

#!/usr/bin/env python3
from typing import Tuple
"""Compute pagnation"""


def index_range(page: int, page_size: int) -> Tuple:

    """A funtion to compute pagenation based of the args
        Arg:
            page (int) page number
            page_size (Int) number of rows
    """
    start_index = (page - 1) * page_size + 1
    end = start_index + page_size - 1
    start_index -= 1
    return start_index, end

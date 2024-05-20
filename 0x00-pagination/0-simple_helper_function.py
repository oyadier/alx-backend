#!/usr/bin/env python3
from typing import Tuple
"""Compute pagnation"""


def index_range(page: int, page_size: int) -> Tuple:

    """
    index_range: A funtion to compute pagenation based of the args
        Args:
            page (int) page number
            page_size (Int) number of rows
    """
    start_index = page * page_size
    return start_index - page_size, start_index

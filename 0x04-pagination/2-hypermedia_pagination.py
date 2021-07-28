#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments (and defaults) as
get_page and returns a dictionary containing the following key-value pairs:

    * page_size: the length of the returned dataset page
    * page: the current page number
    * data: the dataset page (equivalent to return from previous task)
    * next_page: number of the next page, None if no next page
    * prev_page: number of the previous page, None if no previous page
    * total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        page_index = index_range(page, page_size)
        return self.dataset()[page_index[0]:page_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing the following key-value pairs:
            * page_size: the length of the returned dataset page
            * page: the current page number
            * data: the dataset page (equivalent to return from previous task)
            * next_page: number of the next page, None if no next page
            * prev_page: number of the previous page, None if no previous page
            * total_pages: the total number of pages in the dataset as an int
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        page_index = index_range(page, page_size)
        return {
            "page_size": len(self.dataset()[page_index[0]:page_index[1]]),
            "page": page,
            "data": self.dataset()[page_index[0]:page_index[1]],
            "next_page": None if page == math.ceil(
                len(self.dataset())/page_size) else page + 1,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": math.ceil(len(self.dataset())/page_size)
        }

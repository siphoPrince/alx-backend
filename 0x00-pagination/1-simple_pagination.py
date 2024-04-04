#!/usr/bin/env python3
"""takes two integer arguments"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a specific page of the dataset."""
        assert isinstance(page, int) and page > 0, "must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "must be positive"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        total_rows = len(dataset)

        if end_index > total_rows:
            return []
        return dataset[start_index:end_index]

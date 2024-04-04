#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves a page of data with hypermedia information, considering.

        Args:
            index: The starting index for the requested page (optionalto None).
            page_size: The number of items per page (defaults to 10).

        Returns:
            A dictionary containing pagination metadata and data.
        """
        assert index is None or (0 <= index < len(self.dataset())), "datasets"

        self.indexed_dataset()

        if index is None:
            start_index = 0
        else:
            previous_page_size = page_size
            previous_end_index = index + previous_page_size
            start_index = min(previous_end_index, len(self.dataset()))

        end_index = min(start_index + page_size, len(self.dataset()))
        next_index = end_index

        data = [self.__indexed_dataset[i] for i in range(start_index,
            end_index)]

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }

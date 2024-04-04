#!/usr/bin/env python3
"""get_hyper method that takes the same arguments"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns pagination metadata and the requested page of data."""
        data = self.get_page(page, page_size)

        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

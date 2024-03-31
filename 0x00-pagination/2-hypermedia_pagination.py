#!/usr/bin/env python3
"""get_hyper method that takes the same arguments"""


import math

class Server:
    def __init__(self):
        # Initialize your server or any required attributes
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        """
        Simulates fetching a page of data from a server.
        Returns a list of data items.
        """
        # Implement your logic to fetch the page data here
        pass

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary with hypermedia pagination information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(data) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

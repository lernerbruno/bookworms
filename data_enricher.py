"""Contains the Data Enricher class, which adds new data via selected APIs.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import requests
# 'action=parse&section=0&prop=text&page=pizza'

class Data_Enricher:
    """"""
    def __init__(self, author):
        self.root_url = r'http://en.wikipedia.org/w/api.php?'
        self.author = author
        self.text = self._get_page_content()
        self.uris = []

    def _set_page(self):
        pass

    def _get_page_content(self):
        """Pulls the whole url's HTML as string."""
        url = self.root_url + ''.join(self.uris)
        r = requests.get()
        print(r.text)

Data_Enricher('Carlos')


"""Contains the Data Enricher class, which adds new data via selected APIs.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import requests
import json
from bs4 import BeautifulSoup


class DataEnricher:
    """Enriches the data with Wikipedia information about the author. Return
    the author's year of birth, gender, ethnic group and country of
    nationality. """

    def __init__(self):
        self.PROP_NAME = 0
        self.PROP_NUM = 1

    def get_properties(self, author_name):
        try:
            data_id = self.get_data_id(author_name)
        except KeyError:
            return {}
        properties = [('year', 'P569'),
                      ('gender', 'P21'),
                      ('ethnic_group', 'P172'),
                      ('country', 'P27')]
        author_props = {}
        for prop in properties:
            result = self.get_prop_info(data_id, prop)
            author_props[prop[self.PROP_NAME]] = result
        return author_props

    def get_data_id(self, author_name):
        ROOT_URL = r'https://en.wikipedia.org/w/api.php?action=query&prop=' \
                   r'pageprops&ppprop=wikibase_item&redirects=1&format=' \
                   r'json&titles='
        full_url = ''.join((ROOT_URL, author_name))
        raw = requests.get(full_url).text
        info_dict = json.loads(raw)['query']['pages']
        page_id = list(info_dict.keys())[0]
        data_id = info_dict[page_id]['pageprops']['wikibase_item']
        return data_id

    def get_prop_info(self, data_id, prop):
        ROOT_URL = r'https://www.wikidata.org/w/api.php?action=wbgetclaims' \
                   r'&format=json&property={}&entity={}'
        WIKIDATA_URL = 'https://www.wikidata.org/wiki/'
        raw = requests.get(ROOT_URL.format(prop[self.PROP_NUM], data_id)).text
        info_dict = json.loads(raw)['claims']
        if info_dict == {}:
            result = 'None'
        if prop[self.PROP_NAME] == 'year':
            birth_date = info_dict[prop[self.PROP_NUM]][0]["mainsnak"] \
                ["datavalue"]["value"]["time"]
            result = birth_date[1:5]
        else:
            wiki_data_id = info_dict[prop[self.PROP_NUM]][0]["mainsnak"] \
                ["datavalue"]["value"]["id"]
            html = requests.get(''.join((WIKIDATA_URL, wiki_data_id))).text
            soup = BeautifulSoup(html, 'lxml')
            result = soup.find('title').contents[0][:-11]
        return result


author = 'Edgar Allan Poe'
enricher = DataEnricher()
print(enricher.get_properties(author))

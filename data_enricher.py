"""Contains the Data Enricher class, which adds new data via selected APIs.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import requests
import json
from bs4 import BeautifulSoup


class DataEnricher:
    """Enriches the data with Wikipedia information about the author. Return
    the author's year of birth, gender, ethnic group and country of
    nationality. """
    PROP_NAME = 0
    PROP_NUM = 1
    WIKI_API_URL = r'https://en.wikipedia.org/w/api.php?action' \
                   r'=query&prop=pageprops&ppprop=wikibase_item' \
                   r'&redirects=1&format=json&titles='
    WIKIDATA_API_URL = r'https://www.wikidata.org/w/api.php?action=' \
                       r'wbgetclaims&format=json&property={}&entity={}'
    WIKIDATA_URL = 'https://www.wikidata.org/wiki/'

    def __init__(self):
        pass

    @classmethod
    def get_extra_data(cls, author_name):
        """Fetches information about the author from Wikidata API, returning a
        dictionary."""
        try:
            data_id = cls._get_data_id(author_name)
        except KeyError:
            return {'year': None, 'gender': None, 'ethnic_group': None,
                    'country': None}
        properties = [('year', 'P569'),
                      ('gender', 'P21'),
                      ('ethnic_group', 'P172'),
                      ('country', 'P27')]
        author_props = {}
        for prop in properties:
            result = cls._get_prop_info(data_id, prop)
            author_props[prop[cls.PROP_NAME]] = result
        return author_props

    @classmethod
    def _get_data_id(cls, author_name):
        """Gets the Wikidata id for the author.
        Look into the Wikidata API documentation for further information."""
        full_url = ''.join((cls.WIKI_API_URL, author_name))
        raw = requests.get(full_url).text
        info_dict = json.loads(raw)['query']['pages']
        page_id = list(info_dict.keys())[0]
        data_id = info_dict[page_id]['pageprops']['wikibase_item']
        return data_id

    @classmethod
    def _get_prop_info(cls, data_id, prop):
        """Using the author Wikidata id, returns the info of the specified
        property. """
        raw = requests.get(
            cls.WIKIDATA_API_URL.format(prop[cls.PROP_NUM], data_id)).text
        info_dict = json.loads(raw)['claims']
        if info_dict == {}:
            result = None
        elif prop[cls.PROP_NAME] == 'year':
            birth_date = info_dict[prop[cls.PROP_NUM]][0]["mainsnak"] \
                ["datavalue"]["value"]["time"]
            try:
                result = int(birth_date[
                         birth_date.index('+') + 1:birth_date.index('-')])
            except ValueError:      # If no year is found
                result = None
        else:
            wiki_data_id = info_dict[prop[cls.PROP_NUM]][0]["mainsnak"] \
                ["datavalue"]["value"]["id"]
            html = requests.get(''.join((cls.WIKIDATA_URL,
                                         wiki_data_id))).text
            soup = BeautifulSoup(html, 'html.parser')
            result = soup.find('title').contents[0][:-11]
        return result

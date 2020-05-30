import os
import json
import collections
from core.utils import tokenize
from settings import BOOK_DATA_FILEPATH


class Storage:
    '''A singleton class to create index storage object

    This is an storage to keep inverted index data
    storage structure:
       {'term': {
           'frequency': 1,
           'documents': {<book_id_1>: <frequency in doc 1>,
                         <book_id_2>: <frequency in doc 2>, ...}
    }}
    '''
    __instance = None

    def __init__(self):
        if Storage.__instance is None:
            Storage.__instance = self
            self.storage = collections.defaultdict(dict)
        else:
            raise Exception('Cannot instantiate another instance of this class.')  # noqa

    @classmethod
    def get_instance(self):
        if Storage.__instance is None:
            Storage()
        return Storage.__instance


class Index:
    '''Create an Inverted index.'''

    def __init__(self, storage):
        self.storage = storage.storage

    def index_book(self, book):
        book_id = book['id']
        summary = book['summary']
        tokens = tokenize(summary)
        for token in tokens:
            if 'frequency' in self.storage[token]:
                self.storage[token]['frequency'] += 1
            else:
                self.storage[token]['frequency'] = 1
            if 'documents' not in self.storage[token]:
                self.storage[token]['documents'] = {}
            if book_id not in self.storage[token]['documents']:
                self.storage[token]['documents'][book_id] = 0
            self.storage[token]['documents'][book_id] += 1

    def index(self, data):
        for book in data['summaries']:
            self.index_book(book)


def remove_punctuations(text):
    pass


def process_text():
    pass


def generate_tokens():
    pass


def remove_stopwords():
    pass


def index_book_data():
    if not os.path.exists(BOOK_DATA_FILEPATH):
        raise FileNotFoundError('book data file not found')
    data = json.load(open(BOOK_DATA_FILEPATH))

    storage = Storage.get_instance()
    index = Index(storage)

    index.index(data)

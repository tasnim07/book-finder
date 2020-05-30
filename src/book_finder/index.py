import os
import json
import collections
from core.utils import tokenize
from settings import BOOK_DATA_FILEPATH


class Storage:
    '''A singleton class to create index storage object

    This can act like an in-memory database.
    This is an storage to keep inverted index data.
    inverted index structure:
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
            self.inverted_index = collections.defaultdict(dict)
            self.books = collections.defaultdict(dict)
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
        self.storage_obj = storage
        self.inverted_index = storage.inverted_index

    def index_book(self, book):
        '''Index single book instance.'''
        book_id = book['id']
        if self.storage_obj.books.get(book_id):
            # if book is already there in storage, that means it is already indexed.  # noqa
            # update we can handle separately
            # exit the method gracefully.
            return

        summary = book['summary']
        tokens = tokenize(summary)
        for token in tokens:
            if 'frequency' in self.inverted_index[token]:
                self.inverted_index[token]['frequency'] += 1
            else:
                self.inverted_index[token]['frequency'] = 1
            if 'documents' not in self.inverted_index[token]:
                self.inverted_index[token]['documents'] = {}
            if book_id not in self.inverted_index[token]['documents']:
                self.inverted_index[token]['documents'][book_id] = 0
            self.inverted_index[token]['documents'][book_id] += 1

        self.storage_obj.books[book_id] = book

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

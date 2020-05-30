import os
import json
import collections


# this is an storage to keep indexed data
'''
structure:
{'term': {
    'frequency': 1,
    'documents': {<book_id_1>: <frequency in doc 1>,
                  <book_id_2>: <frequency in doc 2>, ...}
}}
'''
storage = collections.defaultdict(dict)


def index(data):
    for book in data['summaries']:
        book_id = book['id']
        summary = book['summary']
        tokens = summary.lower().split()
        for token in tokens:
            if 'frequency' in storage[token]:
                storage[token]['frequency'] += 1
            else:
                storage[token]['frequency'] = 1
            if 'documents' not in storage[token]:
                storage[token]['documents'] = {}
            if book_id not in storage[token]['documents']:
                storage[token]['documents'][book_id] = 0
            storage[token]['documents'][book_id] += 1


def remove_punctuations(text):
    pass


def process_text():
    pass


def generate_tokens():
    pass


def remove_stopwords():
    pass


def index_book_data():
    BOOK_DATA_FILEPATH = '../data.json'  # put this under .env
    if not os.path.exists(BOOK_DATA_FILEPATH):
        raise FileNotFoundError('book data file not found')
    data = json.load(open(BOOK_DATA_FILEPATH))

    index(data)

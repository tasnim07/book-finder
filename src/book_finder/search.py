from book_finder.index import storage
from core.utils import tokenize
from core.exceptions import IndexNotFoundError


def search(query):
    '''
    Search the index by tokenizing each word.

    # Args:
      - query(str) - the text to query for
    '''
    if not isinstance(query, str):
        raise ValueError('query should be str')
    if not storage:
        raise IndexNotFoundError()
    query_tokens = tokenize(query)

    token_docs = []
    for token in query_tokens:
        token_docs.append(set(storage.get(token, {}).get('documents', [])))

    return list(set.intersection(*token_docs))


def score():
    pass


def get_term_frequency():
    pass


def get_idf():
    pass


# we can use decorator pattern to calculate score

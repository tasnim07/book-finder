import unittest
from book_finder import search
from book_finder import index
from core.exceptions import IndexNotFoundError


def test_search_arguments():
    '''search function only supports string input.'''
    case = unittest.TestCase()
    with case.assertRaises(ValueError):
        search.Search(['take your book'])


def test_search_index_existence():
    '''Test wether the search index defined and populated.'''
    case = unittest.TestCase()
    with case.assertRaises(IndexNotFoundError):
        search.Search('take your book')


def test_search_book():
    test_data = {
        'summaries': [
            {
                'id': 0,
                'summary': 'Anything You Want man'
            },
            {
                'id': 1,
                'summary': 'The Richest Man in Babylon merchant son'
            },
            {
                'id': 2,
                'summary': 'Letters from a Self-Made Merchant to His Son'
            },
            {
                'id': 3,
                'summary': 'The Nurture Assumption of self-made man'
            },
        ]
    }
    storage = index.Storage.get_instance()
    index_obj = index.Index(storage)
    index_obj.index(test_data)

    search_obj = search.Search('man')
    assert search_obj.search() == [0, 1, 3]

    search_obj = search.Search('merchant')
    assert search_obj.search() == [1, 2]

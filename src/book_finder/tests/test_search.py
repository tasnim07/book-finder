import unittest
from book_finder import search
from book_finder import index
from core.exceptions import IndexNotFoundError


def test_search_arguments():
    '''search function only supports string input.'''
    case = unittest.TestCase()
    with case.assertRaises(ValueError):
        search.search(['take your book'])


def test_search_index_existence():
    '''Test wether the search index defined and populated.'''
    case = unittest.TestCase()
    with case.assertRaises(IndexNotFoundError):
        search.search('take your book')


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
    index.index(test_data)

    search_result = search.search('man')
    assert search_result == [0, 1, 3]

    search_result = search.search('merchant')
    assert search_result == [1, 2]

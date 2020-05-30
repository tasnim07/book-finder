'''Module: Define all scoring classes to be used in search'''
import abc
import math
from book_finder.index import Storage


class AbstractBaseScore(abc.ABC):

    @abc.abstractmethod
    def calculate(self, text_tokens, book_id):
        pass


class TermFrequencyScore(AbstractBaseScore):
    '''Term Frequency (tf) calculator.

    This is the square root of the number of times the term appears in the
    field of a document:

        `tf = sqrt(termFreq)`
    '''

    def calculate(self, text_tokens, book_id):
        # pass each book and calculate its tf
        storage = Storage.get_instance()
        book = storage.books.get(book_id)
        score = 0
        for token in text_tokens:
            term_frequency = book['summary'].count(token)
            score += math.sqrt(term_frequency)
        return score


class InverseDocumentFrequencyScore(AbstractBaseScore):
    '''Inverse Document Frequency (idf) calculator.

    This is one plus the natural log of the documents in the index
    divided by the number of documents that contain the term:

        `idf = 1 + ln(total_doc/(docFreq + 1))`

    '''

    def calculate(self, text_tokens, book_id):
        storage = Storage.get_instance()
        total_book_count = len(storage.books)
        score = 0
        for token in text_tokens:
            doc_freq = len(storage.inverted_index[token].get('documents', {}))
            score += (1 + math.log(total_book_count / (doc_freq + 1)))
        return score

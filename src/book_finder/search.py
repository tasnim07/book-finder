from book_finder.index import Storage
from core.utils import tokenize
from core.exceptions import IndexNotFoundError
from book_finder.scoring import TermFrequencyScore, \
    InverseDocumentFrequencyScore


class Search:

    scoring_classes = [TermFrequencyScore, InverseDocumentFrequencyScore]

    def __init__(self, text, k=3):
        '''Args:
              text (str): text is a search text.
        '''
        if not isinstance(text, str):
            raise ValueError('text should be str')
        self.storage_obj = Storage.get_instance()
        if not self.storage_obj.inverted_index:
            raise IndexNotFoundError()

        self.inverted_index = self.storage_obj.inverted_index

        self.text = text
        self.k = k
        self.text_tokens = tokenize(text)

    def search(self):
        '''Search the index and get the relevant result.'''
        if not isinstance(self.text, str):
            raise ValueError('search text should be str')

        token_docs = []
        for token in self.text_tokens:
            token_docs.append(
                set(self.inverted_index.get(token, {}).get('documents', {}))
            )

        return list(set.intersection(*token_docs))

    def get_search_response(self, scored_result):
        '''prepare response for each book object.'''
        summaries = []
        for scored_book in scored_result:
            book = self.storage_obj.books[scored_book['book_id']]
            summaries.append(book)

        return summaries

    def get_result(self):
        '''Get final result'''
        search_result = self.search()
        scored_result = self.calculate_score(search_result)
        return self.get_search_response(scored_result)[:self.k]

    def calculate_score(self, search_result):
        '''Calculate score of each relevant search result'''
        # result stores book_id and score mapping
        result = []
        for book_id in search_result:
            score = 0
            for scoring_class in self.scoring_classes:
                score += scoring_class().calculate(self.text_tokens, book_id)
            result.append({'book_id': book_id, 'score': score})

        return sorted(result, key=lambda x: x['score'], reverse=True)

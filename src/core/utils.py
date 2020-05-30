import string
from core.constants import STOPWORDS


def tokenize(sent, is_lower=True, remove_stopwords=True):
    if is_lower:
        sent = sent.lower()

    # remove punctuation from each word.
    table = str.maketrans('', '', string.punctuation)
    tokens = []
    for word in sent.split():
        word = word.translate(table)
        if remove_stopwords:
            if word not in STOPWORDS:
                tokens.append(word)
        else:
            tokens.append(word)

    return tokens

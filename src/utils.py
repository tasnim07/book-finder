def tokenize(sent, is_lower=True, remove_stopwords=False,
             remove_punctuations=False):
    if is_lower:
        sent = sent.lower()
    return sent.split()

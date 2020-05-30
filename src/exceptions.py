
class IndexNotFoundError(Exception):
    default_message = 'data is not indexed. Please index first'

    def __init__(self, msg=default_message, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

from json import dumps


class Result:
    def __init__(self):
        pass

    """Universal results"""

    # 1000-1999
    SUCCESS = 1000  # Used generically any time the expected outcome is achieved

    # 9000-999
    INVALID_PARAMETER = 9000  # Used any time a parameter is invalid or missing
    POST_ONLY = 9001  # Used any time a POST-only method is requested by an HTTP method other than POST (GET, PUT, etc.)
    GET_ONLY = 9002  # Generally not used, as Chimera's API is intended to be accessible only by POST
    DATABASE_CANNOT_SAVE = 9003  # Used generically when an item cannot be saved to the database
    DATABASE_ENTRY_NOT_FOUND = 9004  # Used when a request is made for a database entry which does not exist

    """Method-specific results"""

    # 2000-2009 /user
    EMAIL_IN_USE = 2000  # Used when a request for /user/create uses an existing email address

    # 2040-2049 /blog
    HYDRA_ERROR = 2040  # Used generically when an error is received from Hydra
    DATABASE_CANNOT_SAVE_ALBUM = 2041  # Used in Hydra when an album model cannot be saved to the database
    DATABASE_CANNOT_SAVE_BLOB = 2042  # Used in Hydra when a blob model cannot be saved to the database
    STORAGE_CANNOT_SAVE_BLOB = 2043  # Used in Hydra when a blob cannot be saved to storage

    # 2050-2059 /blog/delete
    STORAGE_CANNOT_DELETE_BLOB = 2050  # Used in Hydra when a blob cannot be deleted from storage
    DATABASE_CANNOT_DELETE_BLOB = 2051  # Used in Hydra when a blob cannot be deleted from the database
    DATABASE_CANNOT_DELETE_ALBUM = 2052  # Used in Hydra when an album cannot be deleted from the database

    # 2060-2069 /post/delete
    DATABASE_CANNOT_DELETE_POST = 2060  # Used when a post cannot be deleted from the database

    # 2070-2079 /order/delete
    DATABASE_CANNOT_DELETE_ORDER = 2070  # Used when an order cannot be deleted from the database

    # Result dictionary used internally only. Empty string for message means no message member is returned
    _result = {

        # 1000-1999
        SUCCESS: '',

        # 9000-9999
        INVALID_PARAMETER: 'Invalid parameter',
        POST_ONLY: 'This method is only accessible by POST',
        GET_ONLY: 'This method is only accessible by GET',
        DATABASE_CANNOT_SAVE: 'Cannot save to database',
        DATABASE_ENTRY_NOT_FOUND: 'Database entry not found',

        # 2000-2009
        EMAIL_IN_USE: 'Email already in use',

        # 2040-2049
        HYDRA_ERROR: 'Unknown error from Hydra',
        DATABASE_CANNOT_SAVE_ALBUM: 'Album cannot be saved to database',
        DATABASE_CANNOT_SAVE_BLOB: 'Blob cannot be saved to database',
        STORAGE_CANNOT_SAVE_BLOB: 'Blob cannot be saved to storage',

        # 2050-2059
        STORAGE_CANNOT_DELETE_BLOB: 'Blob cannot be deleted from storage',
        DATABASE_CANNOT_DELETE_BLOB: 'Blob cannot be deleted from database',
        DATABASE_CANNOT_DELETE_ALBUM: 'Album cannot be deleted from database',

        # 2060-2069
        DATABASE_CANNOT_DELETE_POST: 'Post cannot be deleted from database',

        # 2070-2079
        DATABASE_CANNOT_DELETE_ORDER: 'Order cannot be deleted from database',
    }

    @staticmethod
    def append_result(dictionary, result):
        dictionary['result'] = result
        if Result._result.get(result):
            dictionary['message'] = Result._result.get(result)

    @staticmethod
    def get_result_dump(result):
        dictionary = {}
        Result.append_result(dictionary, result=result)
        return dumps(dictionary)

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
    DATABASE_ENTRY_NOT_FOUND = 9004  # Used when a request is made for a database entry which does not exist

    """Method-specific results"""

    # 2000-2009 /user
    EMAIL_IN_USE = 2000  # Used when a request for /user/create uses an existing email address

    # 2040-2049 /blog
    HYDRA_ERROR = 2040  # Used generically when an error is received from Hydra
    DATABASE_CANNOT_SAVE_ALBUM = 2041  # Used in Hydra when an album model cannot be saved to the database
    DATABASE_CANNOT_SAVE_BLOB = 2042  # Used in Hydra when a blob model cannot be saved to the database
    GCS_CANNOT_SAVE_BLOB = 2043  # Used in Hydra when a blob cannot be saved to gcs

    Result = (
        (SUCCESS, ''),
        (INVALID_PARAMETER, 'Invalid parameter'),
        (POST_ONLY, 'This method is only accessible by POST'),
        (GET_ONLY, 'This method is only accessible by GET'),
        (DATABASE_ENTRY_NOT_FOUND, 'Database entry not found'),
    )

    @staticmethod
    def message(result):
        return Result.Result[result][1]

class StorageURLSuffixes:
    def __init__(self):
        pass

    USER_PROFILE_PHOTO = 0
    SIREN_BLOG = 1
    POST = 2

    _suffixes = {
        USER_PROFILE_PHOTO: 'user/profile-photo/',
        SIREN_BLOG: 'siren/blog/',
        POST: 'post/',
    }

    @staticmethod
    def get_url_suffix(storage_url_suffix):
        suffix = StorageURLSuffixes.get_url_suffixes().get(storage_url_suffix)
        return suffix

    @staticmethod
    def get_url_suffixes():
        suffixes = StorageURLSuffixes._suffixes
        return suffixes

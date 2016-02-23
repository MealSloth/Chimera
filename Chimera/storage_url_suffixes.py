class StorageURLSuffixes:
    def __init__(self):
        pass

    USER_PROFILE_PHOTO = 0
    SIREN_BLOG = 1

    _storage_url_suffixes = {
        USER_PROFILE_PHOTO: 'user/profile-photo/',
        SIREN_BLOG: 'siren/blog/',
    }

    @staticmethod
    def get_url_suffix(storage_url_suffix):
        return StorageURLSuffixes._storage_url_suffixes.get(storage_url_suffix)

    @staticmethod
    def get_url_suffixes():
        return StorageURLSuffixes._storage_url_suffixes

from lib import gcs_oauth2_boto_plugin
from lib.boto import boto


GOOGLE_STORAGE = 'gs'

LOCAL_FILE = 'file'

CLIENT_ID = 'mealsloth-chimera-ap01-cloudstorage-bu01'
CLIENT_SECRET = '3i8tSK69upv1aWEW0tCxBwj0/HST0/ladjxNpjG8'

gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)


def save_blob(blob_id, file_post):
    dst_uri = boto.storage_uri(
        CLIENT_ID + '/' + str(blob_id), GOOGLE_STORAGE)
    dst_uri.new_key().set_contents_from_file(file_post)
    print 'Successfully created "%s/%s"' % (dst_uri.bucket_name, dst_uri.object_name)

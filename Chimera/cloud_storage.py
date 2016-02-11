# #!/usr/bin/python
#
# from lib import gcs_oauth2_boto_plugin
# from lib import boto
#
# GOOGLE_STORAGE = 'gs'
#
# CLIENT_ID = '265360872473-2hhoa60jmo32flkfn4pbaf5og138gc9s.apps.googleusercontent.com'
# CLIENT_SECRET = '58qDd-7TqjKbIF7jKb6KTPm4'
# gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)
#
# BUCKET = 'mealsloth-chimera-ap01-cloudstorage-bu01'
#
#
# def save_blob(directory, name, content):
#     dst_uri = boto.storage_uri(BUCKET + '/' + directory + name, GOOGLE_STORAGE)
#     dst_uri.new_key().set_contents_from_file(content)
#     print 'Successfully created "%s/%s"' % (dst_uri.bucket_name, dst_uri.object_name)

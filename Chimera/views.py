from view.album import view_album_delete
from view.blob import view_blob_bucket_url, view_blob_delete, view_blob_upload, view_blob
from view.order import view_order_delete
from view.post import view_post, view_post_delete
from view.user import view_user, view_user_create
from view.user_login import view_user_login
from django.http import HttpResponse
from json import dumps
import jobs


# home

# /
def home(request):  # /
    response = dumps({
        'message': 'This is the MealSloth API. If you would like to learn more about MealSloth, please visit the URL.',
        'url': 'mealsloth.com',
    })
    return HttpResponse(response, content_type='application/json')


# album

# /album/delete
def album_delete(request):  # /album/delete
    return view_album_delete.album_delete(request)


# blob

# /blob/bucket
def blob_bucket_url(request):  # /blob/bucket/url
    return view_blob_bucket_url.blob_bucket_url(request)


# /blob/upload
def blob_upload(request):  # /blob/upload
    return view_blob_upload.blob_upload(request)


# /blob/delete
def blob_delete(request):
    return view_blob_delete.blob_delete(request)


# blob/view
def blob(request):  # /blob/view
    return view_blob.blob(request)


# user

# /user
def user(request):  # /user
    return view_user.user(request)


# /user/create
def user_create(request):  # /user/create
    return view_user_create.user_create(request)


# order

# order/delete/
def order_delete(request):
    return view_order_delete.order_delete(request)


# post

# /post
def post(request):  # /post
    return view_post.post(request)


# /post/delete
def post_delete(request):
    return view_post_delete.post_delete(request)


# user-login

# /user-login
def user_login(request):  # /user-login
    return view_user_login.user_login(request)


# job

# /job/post
def job_post_status(request):  # /job/post/status
    return jobs.job_post_status()


# /job/post/order
def job_post_order_count(request):  # /job/post/order/count
    return jobs.job_post_order_count()


# /job/order
def job_order_status(request):  # /job/order/status
    return jobs.job_order_status()

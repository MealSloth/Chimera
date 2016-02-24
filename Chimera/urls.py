from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',


    # home

    # /
    url(r'^$', views.home, name='/'),


    # album

    # /album/create/   ## INTERNAL
    # url(r'^album/create/', views.album_create, name='album/create/'),

    # /album/delete/
    url(r'^album/delete/', views.album_delete, name='album/delete/'),


    # blob

    # /blob/bucket/
    url(r'^blob/bucket/url/', views.blob_bucket_url, name='blob/bucket/url/'),

    # /blob/upload/
    url(r'^blob/upload/', views.blob_upload, name='blob/upload/'),

    # /blob/delete/
    url(r'blob/delete/', views.blob_delete, name='blob/delete/'),

    # /blob/view/
    url(r'^blob/', views.blob, name='blob/'),


    # user

    # /user/modify/
    url(r'^user/modify/', views.user_modify, name='user/modify/'),

    # /user/create/
    url(r'^user/create/', views.user_create, name='user/create/'),

    # /user/delete/  ## INTERNAL
    # url(r'^user/delete/', views.user_delete, name='user/delete/'),

    # /user/
    url(r'^user/', views.user, name='user/'),


    # user_login

    # /user_login/
    url(r'^user-login/', views.user_login, name='user-login/'),


    # order

    # /order/create/
    url(r'^order/create/', views.order_create, name='order/create/'),

    # /order/delete/  ## INTERNAL
    # url(r'^order/delete/', views.order_delete, name='order/delete/'),


    # post

    # /post/create/
    url(r'^post/create/', views.post_create, name='post/create/'),

    # /post/delete/  ## INTERNAL
    # url(r'^post/delete/', views.post_delete, name='post/delete/'),

    # /post/
    url(r'^post/', views.post, name='post/'),


    # job

    # /job/post/
    url(r'^job/post/status/', views.job_post_status, name='job/post/status/'),
    url(r'^job/post/order/count/', views.job_post_order_count, name='job/post/order/count/'),

    # /job/order/
    url(r'^job/order/status/', views.job_order_status, name='job/order/status/'),
)

from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',


    # home

    url(r'^$', views.home, name='home'),


    # blob

    # blob/bucket
    url(r'^blob/bucket/url', views.blob_bucket_url, name='blob/bucket/url'),

    # blob/upload
    url(r'^blob/upload/album/', views.blob_upload_album, name='blob/upload/album'),
    url(r'^blob/upload/', views.blob_upload, name='blob/upload'),

    # blob/view
    url(r'^blob/view', views.blob_view, name='blob/view'),


    # blog

    url(r'^blog/upload/image/', views.blog_upload_image, name='blog/upload/image'),


    # user

    # user/$
    url(r'^user/', views.user, name='user/$'),
    url(r'^user/', views.user_model_from_id, name='user/$'),

    # user/create
    url(r'^user/create/', views.user_create, name='user/create'),


    # user_login

    url(r'^user-login/', views.user_login, name='user-login'),
    url(r'^user-login/', views.user_login_model_from_id, name='user-login'),


    # post

    # post/$
    url(r'^post/', views.post, name='post/$'),


    # jobs

    # job/post
    url(r'^job/post/status/', views.job_post_status, name='job-post-status'),

    # job/order
    url(r'^job/order/status/', views.job_order_status, name='job-order-status'),
)

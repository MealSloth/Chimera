from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^blob-image-upload/', views.blob_image_upload, name='blob-image-upload'),
    url(r'^blob-image-view/', views.blob_image_view, name='blob-image-view'),
    url(r'^blog-image-upload/', views.blog_image_upload, name='blog-image-upload'),
    url(r'^user-model-from-id/([^/]+)/', views.user_model_from_id, name='user-model-from-id'),
    url(r'^post-model-from-id/([^/]+)/', views.post_model_from_id, name='post-model-from-id'),
    url(r'^user-model-from-email/([^/]+)/', views.user_model_from_email, name='user-model-from-email'),
    url(r'^user-login-model-from-id/([^/]+)/', views.user_login_model_from_id, name='user-login-model-from-id'),
    url(r'^user-login-model-from-user-id/([^/]+)/', views.user_login_model_from_user_id,
        name='user-login-model-from-user-id'),
    url(r'^create-user-from-model/', views.create_user_from_model, name='create-user-from-model'),
)

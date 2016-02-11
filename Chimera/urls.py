from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^blob-photo-upload/', views.blob_photo_upload, name='test-photo-upload'),
    url(r'^blob-photo-view/', views.blob_photo_view, name='test-photo-view'),
    url(r'^user-model-from-id/([^/]+)/', views.user_model_from_id, name='user-model-from-id'),
    url(r'^post-model-from-id/([^/]+)/', views.post_model_from_id, name='post-model-from-id'),
    url(r'^user-model-from-email/([^/]+)/', views.user_model_from_email, name='user-model-from-email'),
    url(r'^create-user-from-model/', views.create_user_from_model, name='create-user-from-model'),
)

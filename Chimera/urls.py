from django.conf.urls import patterns, url
from Chimera import views

urlpatterns = patterns(
    '',
    url(r'^user-model-from-id/([^/]+)/', views.user_model_from_id, name='user-model-from-id'),
    url(r'^post-model-from-id/([^/]+)/', views.post_model_from_id, name='post-model-from-id'),
    url(r'^user-model-from-email/([^/]+)/', views.user_model_from_email, name='user-model-from-email'),
)

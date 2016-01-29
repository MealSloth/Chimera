from django.conf.urls import patterns, url
from Chimera import views

urlpatterns = patterns(
    '',
    url(r'^user-model-from-id/([^/]+)/', views.user_model_from_id, name='user-model-from-id'),
    url(r'^user-model-from-email/([^/]+)/', views.user_model_from_email, name='user-model-from-email'),
)

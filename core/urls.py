from django.urls import path, include
from .views import HelloView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("hello/", HelloView.as_view()),
    path("token-auth/", obtain_auth_token),
]

from django.urls import path
from users.api.views import UserAPI

urlpatterns = [
    path('users/', UserAPI.as_view()),
]
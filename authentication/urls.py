from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import LoginView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('register', TokenRefreshView.as_view(), name='refresh')
]
